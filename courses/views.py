from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from accounts.decorators import teacher_required

from .forms import (
    CourseForm,
    CourseModeScheduleForm,
    ExamModeForm,
    JoinCourseForm,
    LinkGlossaryForm,
    RosterForm,
)
from .models import Course, CourseGlossary, CourseModeSchedule, Enrollment


def course_for_user(user, pk):
    course = get_object_or_404(Course, pk=pk)
    if course.teacher_id == user.id or user.is_staff:
        return course
    if Enrollment.objects.filter(course=course, student=user, is_active=True).exists():
        return course
    raise PermissionDenied("You are not enrolled in this course.")


@login_required
def course_list(request):
    if request.user.is_teacher:
        courses = request.user.taught_courses.all()
    else:
        courses = Course.objects.filter(
            enrollments__student=request.user, enrollments__is_active=True
        )
    return render(request, "courses/list.html", {"courses": courses.distinct()})


@teacher_required
def course_create(request):
    form = CourseForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        course = form.save(commit=False)
        course.teacher = request.user
        course.save()
        messages.success(request, "Course created.")
        return redirect("courses:detail", pk=course.pk)
    return render(request, "courses/form.html", {"form": form, "title": "Create course"})


@login_required
def course_detail(request, pk):
    course = course_for_user(request.user, pk)
    is_owner = course.teacher_id == request.user.id or request.user.is_staff
    context = {"course": course, "is_owner": is_owner}
    if is_owner:
        context.update(
            {
                "roster_form": RosterForm(),
                "exam_form": ExamModeForm(),
                "schedule_form": CourseModeScheduleForm(),
                "link_form": LinkGlossaryForm(teacher=course.teacher, course=course),
            }
        )
    return render(request, "courses/detail.html", context)


@login_required
def join_course(request):
    form = JoinCourseForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        course = Course.objects.filter(join_code=form.cleaned_data["join_code"]).first()
        if course is None:
            form.add_error("join_code", "No course has that join code.")
        elif course.teacher_id == request.user.id:
            form.add_error("join_code", "You already teach this course.")
        else:
            Enrollment.objects.update_or_create(
                course=course,
                student=request.user,
                defaults={"is_active": True, "native_language": request.user.native_language},
            )
            messages.success(request, f"You joined {course.name}.")
            return redirect("courses:detail", pk=course.pk)
    return render(request, "courses/join.html", {"form": form})


@teacher_required
@require_POST
def roster_create(request, pk):
    course = get_object_or_404(Course, pk=pk, teacher=request.user)
    form = RosterForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data["name"]
        if course.rosters.filter(name=name).exists():
            messages.error(request, "That roster already exists.")
        else:
            roster = form.save(commit=False)
            roster.course = course
            roster.save()
            messages.success(request, "Roster created.")
    else:
        messages.error(request, "The roster could not be created.")
    return redirect("courses:detail", pk=course.pk)


@teacher_required
@require_POST
def exam_mode(request, pk):
    course = get_object_or_404(Course, pk=pk, teacher=request.user)
    action = request.POST.get("action")
    if action == "study":
        course.set_study_mode()
        messages.success(request, "Study Mode is active.")
    else:
        form = ExamModeForm(request.POST)
        if form.is_valid():
            course.mode = Course.Mode.EXAM
            course.exam_mode_until = form.ends_at()
            course.save(update_fields=["mode", "exam_mode_until", "updated_at"])
            messages.success(request, "Exam Mode is active.")
        else:
            messages.error(request, "Choose an Exam Mode duration from 5 to 480 minutes.")
    return redirect("courses:detail", pk=course.pk)


@teacher_required
@require_POST
def schedule_create(request, pk):
    course = get_object_or_404(Course, pk=pk, teacher=request.user)
    form = CourseModeScheduleForm(request.POST)
    if form.is_valid():
        schedule = form.save(commit=False)
        schedule.course = course
        schedule.created_by = request.user
        schedule.full_clean()
        schedule.save()
        messages.success(request, "Exam Mode window scheduled.")
    else:
        messages.error(request, "The Exam Mode window is invalid.")
    return redirect("courses:detail", pk=course.pk)


@teacher_required
@require_POST
def schedule_delete(request, pk, schedule_pk):
    schedule = get_object_or_404(
        CourseModeSchedule, pk=schedule_pk, course_id=pk, course__teacher=request.user
    )
    schedule.delete()
    messages.success(request, "Schedule removed.")
    return redirect("courses:detail", pk=pk)


@teacher_required
@require_POST
def link_glossary(request, pk):
    course = get_object_or_404(Course, pk=pk, teacher=request.user)
    form = LinkGlossaryForm(request.POST, teacher=request.user, course=course)
    if form.is_valid():
        CourseGlossary.objects.get_or_create(course=course, glossary=form.cleaned_data["glossary"])
        messages.success(request, "Glossary linked to course.")
    else:
        messages.error(request, "Select one of your unlinked glossaries.")
    return redirect("courses:detail", pk=course.pk)


@teacher_required
@require_POST
def unlink_glossary(request, pk, link_pk):
    link = get_object_or_404(CourseGlossary, pk=link_pk, course_id=pk, course__teacher=request.user)
    link.delete()
    messages.success(request, "Glossary unlinked.")
    return redirect("courses:detail", pk=pk)
