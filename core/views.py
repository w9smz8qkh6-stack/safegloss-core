from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, "core/home.html")


def health(request):
    return JsonResponse({"status": "ok"})


@login_required
def dashboard(request):
    if request.user.is_teacher:
        courses = request.user.taught_courses.prefetch_related("course_glossaries")
        glossaries = request.user.glossaries.order_by("title")
    else:
        courses = request.user.enrollments.select_related("course").order_by("course__name")
        glossaries = None
    return render(
        request,
        "core/dashboard.html",
        {"courses": courses, "glossaries": glossaries},
    )
