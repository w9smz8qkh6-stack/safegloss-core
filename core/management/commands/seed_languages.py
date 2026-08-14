from django.core.management.base import BaseCommand

from core.models import Language

LANGUAGES = [
    ("ar", "Arabic", "العربية"),
    ("bn", "Bengali", "বাংলা"),
    ("en", "English", "English"),
    ("es", "Spanish", "Español"),
    ("fr", "French", "Français"),
    ("hi", "Hindi", "हिन्दी"),
    ("id", "Indonesian", "Bahasa Indonesia"),
    ("ja", "Japanese", "日本語"),
    ("ko", "Korean", "한국어"),
    ("pt", "Portuguese", "Português"),
    ("ru", "Russian", "Русский"),
    ("th", "Thai", "ไทย"),
    ("tr", "Turkish", "Türkçe"),
    ("uk", "Ukrainian", "Українська"),
    ("ur", "Urdu", "اردو"),
    ("vi", "Vietnamese", "Tiếng Việt"),
    ("zh", "Chinese", "中文"),
]


class Command(BaseCommand):
    help = "Create or update the small built-in language catalog."

    def handle(self, *args, **options):
        for code, name, native_name in LANGUAGES:
            Language.objects.update_or_create(
                code=code,
                defaults={"name": name, "native_name": native_name},
            )
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(LANGUAGES)} languages."))
