from django.urls import path

from . import views

app_name = "glossary"
urlpatterns = [
    path("", views.glossary_list, name="list"),
    path("new/", views.glossary_create, name="create"),
    path("<int:pk>/", views.glossary_detail, name="detail"),
    path("<int:pk>/edit/", views.glossary_update, name="update"),
    path("<int:pk>/terms/new/", views.term_create, name="term-create"),
    path("terms/<int:term_pk>/translate/", views.translation_create, name="translation-create"),
    path("terms/<int:term_pk>/delete/", views.term_delete, name="term-delete"),
    path("<int:pk>/import/", views.import_csv, name="import"),
    path("<int:pk>/export/", views.export_csv, name="export"),
    path("course/<int:course_pk>/<int:pk>/", views.course_view, name="course-view"),
]
