def active_exam_course_for_user(user):
    if not user.is_authenticated or user.is_teacher:
        return None
    enrollments = (
        user.enrollments.filter(is_active=True)
        .select_related("course")
        .prefetch_related("course__mode_schedules")
    )
    for enrollment in enrollments:
        if enrollment.course.is_exam_mode:
            return enrollment.course
    return None
