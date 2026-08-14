from django.urls import path

from . import views

app_name = "courses"
urlpatterns = [
    path("", views.course_list, name="list"),
    path("new/", views.course_create, name="create"),
    path("join/", views.join_course, name="join"),
    path("<int:pk>/", views.course_detail, name="detail"),
    path("<int:pk>/rosters/new/", views.roster_create, name="roster-create"),
    path("<int:pk>/exam-mode/", views.exam_mode, name="exam-mode"),
    path("<int:pk>/schedules/new/", views.schedule_create, name="schedule-create"),
    path(
        "<int:pk>/schedules/<int:schedule_pk>/delete/",
        views.schedule_delete,
        name="schedule-delete",
    ),
    path("<int:pk>/glossaries/link/", views.link_glossary, name="link-glossary"),
    path(
        "<int:pk>/glossaries/<int:link_pk>/unlink/", views.unlink_glossary, name="unlink-glossary"
    ),
]
