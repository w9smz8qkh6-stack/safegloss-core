from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from core.models import Language

from .models import User


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "display_name", "role", "native_language")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["role"].choices = (
            (User.Role.STUDENT, "Student"),
            (User.Role.TEACHER, "Teacher"),
        )
        self.fields["native_language"].queryset = Language.objects.order_by("name")
        self.fields["native_language"].required = False
