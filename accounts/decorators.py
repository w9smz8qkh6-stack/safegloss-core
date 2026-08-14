from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


def teacher_required(view_func):
    @login_required
    @wraps(view_func)
    def wrapped(request, *args, **kwargs):
        if not request.user.is_teacher:
            raise PermissionDenied("Teacher access is required.")
        return view_func(request, *args, **kwargs)

    return wrapped
