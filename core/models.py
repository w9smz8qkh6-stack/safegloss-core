from django.db import models


class Language(models.Model):
    code = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=100)
    native_name = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.native_name or self.name


class Subject(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
