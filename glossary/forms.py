from django import forms

from .models import Glossary, Term, TermTranslation


class GlossaryForm(forms.ModelForm):
    class Meta:
        model = Glossary
        fields = (
            "title",
            "description",
            "source_language",
            "default_target_language",
            "subject",
            "is_public",
        )


class TermForm(forms.ModelForm):
    pronunciation_url = forms.URLField(required=False, assume_scheme="https")

    class Meta:
        model = Term
        fields = (
            "phrase",
            "definition",
            "example",
            "part_of_speech",
            "pronunciation_url",
            "is_exam_approved",
        )


class TranslationForm(forms.ModelForm):
    class Meta:
        model = TermTranslation
        fields = ("language", "text", "example")


class CSVImportForm(forms.Form):
    csv_file = forms.FileField(help_text="UTF-8 CSV, maximum 2 MB.")

    def clean_csv_file(self):
        uploaded = self.cleaned_data["csv_file"]
        if uploaded.size > 2 * 1024 * 1024:
            raise forms.ValidationError("The CSV file must be 2 MB or smaller.")
        if not uploaded.name.lower().endswith(".csv"):
            raise forms.ValidationError("Upload a .csv file.")
        return uploaded
