from django.contrib import admin

from .models import Glossary, Term, TermTranslation


class TermTranslationInline(admin.TabularInline):
    model = TermTranslation
    extra = 0


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ("phrase", "glossary", "is_exam_approved")
    list_filter = ("is_exam_approved",)
    search_fields = ("phrase", "definition")
    inlines = (TermTranslationInline,)


admin.site.register(Glossary)
