import csv
import io

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from accounts.decorators import teacher_required
from core.models import Language
from courses.access import active_exam_course_for_user
from courses.models import CourseGlossary, Enrollment
from courses.views import course_for_user

from .forms import CSVImportForm, GlossaryForm, TermForm, TranslationForm
from .models import Glossary, Term, TermTranslation


def accessible_glossaries(user):
    query = Q(is_public=True)
    if user.is_authenticated:
        query |= Q(creator=user)
        if user.is_teacher:
            query |= Q(course_links__course__teacher=user)
        else:
            query |= Q(
                course_links__course__enrollments__student=user,
                course_links__course__enrollments__is_active=True,
            )
    return Glossary.objects.filter(query).distinct()


def glossary_rows(glossary, language, exam_mode=False):
    terms = glossary.terms.prefetch_related("translations__language")
    if exam_mode:
        terms = terms.filter(is_exam_approved=True)
    rows = []
    for term in terms:
        translation = next(
            (item for item in term.translations.all() if item.language_id == language.id), None
        )
        rows.append({"term": term, "translation": translation})
    return rows


def csv_safe(value):
    text = str(value or "")
    if text.startswith(("=", "+", "-", "@")):
        return "'" + text
    return text


@login_required
def glossary_list(request):
    active_exam_course = active_exam_course_for_user(request.user)
    if active_exam_course:
        return redirect("courses:detail", pk=active_exam_course.pk)
    glossaries = accessible_glossaries(request.user)
    return render(request, "glossary/list.html", {"glossaries": glossaries})


@teacher_required
def glossary_create(request):
    form = GlossaryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        glossary = form.save(commit=False)
        glossary.creator = request.user
        glossary.save()
        messages.success(request, "Glossary created.")
        return redirect("glossary:detail", pk=glossary.pk)
    return render(request, "glossary/form.html", {"form": form, "title": "Create glossary"})


@login_required
def glossary_detail(request, pk):
    glossary = get_object_or_404(accessible_glossaries(request.user), pk=pk)
    active_exam_course = active_exam_course_for_user(request.user)
    if active_exam_course:
        if glossary.course_links.filter(course=active_exam_course).exists():
            return redirect(
                "glossary:course-view",
                course_pk=active_exam_course.pk,
                pk=glossary.pk,
            )
        raise PermissionDenied("Only glossaries for the active exam course are available.")
    if not request.user.is_teacher and glossary.creator_id != request.user.id:
        link = (
            glossary.course_links.filter(
                course__enrollments__student=request.user,
                course__enrollments__is_active=True,
            )
            .select_related("course")
            .first()
        )
        if link:
            return redirect("glossary:course-view", course_pk=link.course_id, pk=glossary.pk)
    rows = glossary_rows(glossary, glossary.default_target_language)
    return render(
        request,
        "glossary/detail.html",
        {"glossary": glossary, "rows": rows, "is_owner": glossary.creator_id == request.user.id},
    )


@teacher_required
def glossary_update(request, pk):
    glossary = get_object_or_404(Glossary, pk=pk, creator=request.user)
    form = GlossaryForm(request.POST or None, instance=glossary)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Glossary updated.")
        return redirect("glossary:detail", pk=glossary.pk)
    return render(request, "glossary/form.html", {"form": form, "title": "Edit glossary"})


@teacher_required
def term_create(request, pk):
    glossary = get_object_or_404(Glossary, pk=pk, creator=request.user)
    form = TermForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        phrase = form.cleaned_data["phrase"]
        if glossary.terms.filter(phrase=phrase).exists():
            form.add_error("phrase", "This glossary already contains that term.")
        else:
            term = form.save(commit=False)
            term.glossary = glossary
            term.save()
            messages.success(request, "Term added.")
            return redirect("glossary:detail", pk=glossary.pk)
    return render(request, "glossary/form.html", {"form": form, "title": "Add term"})


@teacher_required
def translation_create(request, term_pk):
    term = get_object_or_404(Term, pk=term_pk, glossary__creator=request.user)
    form = TranslationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        TermTranslation.objects.update_or_create(
            term=term,
            language=form.cleaned_data["language"],
            defaults={"text": form.cleaned_data["text"], "example": form.cleaned_data["example"]},
        )
        messages.success(request, "Translation saved.")
        return redirect("glossary:detail", pk=term.glossary_id)
    return render(
        request,
        "glossary/form.html",
        {"form": form, "title": f"Translate {term.phrase}"},
    )


@login_required
def course_view(request, course_pk, pk):
    course = course_for_user(request.user, course_pk)
    active_exam_course = active_exam_course_for_user(request.user)
    if active_exam_course and active_exam_course.pk != course.pk:
        raise PermissionDenied("Only the active exam course is available.")
    link = get_object_or_404(CourseGlossary, course=course, glossary_id=pk)
    enrollment = Enrollment.objects.filter(
        course=course, student=request.user, is_active=True
    ).first()
    language = (
        enrollment.native_language
        if enrollment and enrollment.native_language_id
        else link.glossary.default_target_language
    )
    exam_mode = course.is_exam_mode and course.teacher_id != request.user.id
    rows = glossary_rows(link.glossary, language, exam_mode=exam_mode)
    return render(
        request,
        "glossary/course_view.html",
        {
            "course": course,
            "glossary": link.glossary,
            "language": language,
            "rows": rows,
            "exam_mode": exam_mode,
        },
    )


@teacher_required
def import_csv(request, pk):
    glossary = get_object_or_404(Glossary, pk=pk, creator=request.user)
    form = CSVImportForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        try:
            text = form.cleaned_data["csv_file"].read().decode("utf-8-sig")
        except UnicodeDecodeError:
            form.add_error("csv_file", "The CSV must use UTF-8 encoding.")
        else:
            reader = csv.DictReader(io.StringIO(text))
            if not reader.fieldnames or "phrase" not in reader.fieldnames:
                form.add_error("csv_file", "The CSV must include a phrase column.")
            else:
                imported = 0
                try:
                    with transaction.atomic():
                        for line_number, row in enumerate(reader, start=2):
                            if line_number > 5001:
                                raise ValueError("A single import may contain at most 5,000 terms.")
                            phrase = (row.get("phrase") or "").strip()
                            if not phrase:
                                raise ValueError(f"Row {line_number} has no phrase.")
                            term, _ = Term.objects.update_or_create(
                                glossary=glossary,
                                phrase=phrase,
                                defaults={
                                    "definition": (row.get("definition") or "").strip(),
                                    "example": (row.get("example") or "").strip(),
                                    "part_of_speech": (row.get("part_of_speech") or "").strip(),
                                    "is_exam_approved": (row.get("is_exam_approved") or "true")
                                    .strip()
                                    .lower()
                                    in {"1", "true", "yes", "y"},
                                },
                            )
                            translation_text = (row.get("translation") or "").strip()
                            language_code = (
                                row.get("language_code") or glossary.default_target_language.code
                            ).strip()
                            if translation_text:
                                language = Language.objects.filter(code=language_code).first()
                                if language is None:
                                    message = (
                                        f"Unknown language code {language_code!r} "
                                        f"on row {line_number}."
                                    )
                                    raise ValueError(message)
                                TermTranslation.objects.update_or_create(
                                    term=term,
                                    language=language,
                                    defaults={"text": translation_text},
                                )
                            imported += 1
                except ValueError as exc:
                    form.add_error("csv_file", str(exc))
                else:
                    messages.success(request, f"Imported {imported} terms.")
                    return redirect("glossary:detail", pk=glossary.pk)
    return render(request, "glossary/import.html", {"form": form, "glossary": glossary})


@teacher_required
def export_csv(request, pk):
    glossary = get_object_or_404(accessible_glossaries(request.user), pk=pk)
    language = glossary.default_target_language
    rows = glossary_rows(glossary, language)
    response = HttpResponse(content_type="text/csv; charset=utf-8")
    response["Content-Disposition"] = f'attachment; filename="glossary-{glossary.pk}.csv"'
    writer = csv.writer(response)
    writer.writerow(
        ["phrase", "translation", "language_code", "definition", "example", "part_of_speech"]
    )
    for row in rows:
        term = row["term"]
        translation = row["translation"]
        writer.writerow(
            [
                csv_safe(term.phrase),
                csv_safe(translation.text if translation else ""),
                language.code,
                csv_safe(term.definition),
                csv_safe(term.example),
                csv_safe(term.part_of_speech),
            ]
        )
    return response


@teacher_required
@require_POST
def term_delete(request, term_pk):
    term = get_object_or_404(Term, pk=term_pk, glossary__creator=request.user)
    glossary_pk = term.glossary_id
    term.delete()
    messages.success(request, "Term deleted.")
    return redirect("glossary:detail", pk=glossary_pk)
