from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from accounts.forms import EmailAuthenticationForm
from core import views as core_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", core_views.health, name="health"),
    path("", core_views.home, name="home"),
    path("dashboard/", core_views.dashboard, name="dashboard"),
    path("accounts/", include("accounts.urls")),
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=EmailAuthenticationForm,
        ),
        name="login",
    ),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("courses/", include("courses.urls")),
    path("glossaries/", include("glossary.urls")),
]

admin.site.site_header = "SafeGloss administration"
admin.site.site_title = "SafeGloss"
