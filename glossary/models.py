from django.conf import settings
from django.db import models


class Glossary(models.Model):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="glossaries",
    )
    title = models.CharField(max_length=180)
    description = models.TextField(blank=True)
    source_language = models.ForeignKey(
        "core.Language",
        on_delete=models.PROTECT,
        related_name="source_glossaries",
    )
    default_target_language = models.ForeignKey(
        "core.Language",
        on_delete=models.PROTECT,
        related_name="target_glossaries",
    )
    subject = models.ForeignKey(
        "core.Subject",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="glossaries",
    )
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title


class Term(models.Model):
    glossary = models.ForeignKey(Glossary, on_delete=models.CASCADE, related_name="terms")
    phrase = models.CharField(max_length=240)
    definition = models.TextField(blank=True)
    example = models.TextField(blank=True)
    part_of_speech = models.CharField(max_length=80, blank=True)
    pronunciation_url = models.URLField(blank=True)
    is_exam_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("phrase",)
        constraints = [
            models.UniqueConstraint(fields=("glossary", "phrase"), name="unique_glossary_phrase")
        ]

    def __str__(self):
        return self.phrase


class TermTranslation(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name="translations")
    language = models.ForeignKey(
        "core.Language",
        on_delete=models.CASCADE,
        related_name="term_translations",
    )
    text = models.CharField(max_length=500)
    example = models.TextField(blank=True)

    class Meta:
        ordering = ("language__name",)
        constraints = [
            models.UniqueConstraint(fields=("term", "language"), name="unique_term_language")
        ]

    def __str__(self):
        return f"{self.term} — {self.language}"
