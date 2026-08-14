from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from accounts.models import User
from core.models import Language
from courses.models import Course, CourseGlossary, Enrollment
from tests.helpers import SYNTHETIC_TEST_CREDENTIAL

from .models import Glossary, Term, TermTranslation


class GlossaryWorkflowTests(TestCase):
    def setUp(self):
        self.english = Language.objects.create(code="en", name="English")
        self.spanish = Language.objects.create(code="es", name="Spanish")
        self.teacher = User.objects.create_user(
            email="teacher@example.test",
            password=SYNTHETIC_TEST_CREDENTIAL,
            role=User.Role.TEACHER,
        )
        self.student = User.objects.create_user(
            email="student@example.test",
            password=SYNTHETIC_TEST_CREDENTIAL,
            role=User.Role.STUDENT,
            native_language=self.spanish,
        )
        self.glossary = Glossary.objects.create(
            creator=self.teacher,
            title="Biology terms",
            source_language=self.english,
            default_target_language=self.spanish,
        )
        self.course = Course.objects.create(teacher=self.teacher, name="Biology")
        CourseGlossary.objects.create(course=self.course, glossary=self.glossary)
        Enrollment.objects.create(
            course=self.course,
            student=self.student,
            native_language=self.spanish,
        )
        self.approved = Term.objects.create(
            glossary=self.glossary,
            phrase="cell",
            definition="The basic structural unit of life.",
            example="A cell contains cytoplasm.",
            is_exam_approved=True,
        )
        TermTranslation.objects.create(term=self.approved, language=self.spanish, text="célula")
        self.unapproved = Term.objects.create(
            glossary=self.glossary,
            phrase="mitochondrion",
            definition="An organelle.",
            is_exam_approved=False,
        )

    def test_student_view_uses_preferred_translation(self):
        self.client.force_login(self.student)
        response = self.client.get(
            reverse("glossary:course-view", args=[self.course.pk, self.glossary.pk])
        )
        self.assertContains(response, "célula")
        self.assertContains(response, "The basic structural unit of life")

    def test_exam_mode_hides_unapproved_terms_and_study_content(self):
        self.course.mode = Course.Mode.EXAM
        self.course.save()
        self.client.force_login(self.student)
        response = self.client.get(
            reverse("glossary:course-view", args=[self.course.pk, self.glossary.pk])
        )
        self.assertContains(response, "célula")
        self.assertNotContains(response, "mitochondrion")
        self.assertNotContains(response, "The basic structural unit of life")
        self.assertNotContains(response, "A cell contains cytoplasm")

    def test_direct_student_link_redirects_to_course_context(self):
        self.client.force_login(self.student)
        response = self.client.get(reverse("glossary:detail", args=[self.glossary.pk]))
        self.assertRedirects(
            response,
            reverse("glossary:course-view", args=[self.course.pk, self.glossary.pk]),
        )

    def test_student_cannot_add_term(self):
        self.client.force_login(self.student)
        response = self.client.get(reverse("glossary:term-create", args=[self.glossary.pk]))
        self.assertEqual(response.status_code, 403)

    def test_duplicate_term_returns_form_error(self):
        self.client.force_login(self.teacher)
        response = self.client.post(
            reverse("glossary:term-create", args=[self.glossary.pk]),
            {"phrase": self.approved.phrase, "is_exam_approved": "on"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "already contains that term")

    def test_csv_import_is_atomic_when_language_is_unknown(self):
        self.client.force_login(self.teacher)
        upload = SimpleUploadedFile(
            "terms.csv",
            b"phrase,translation,language_code\natom,atomo,xx\n",
            content_type="text/csv",
        )
        response = self.client.post(
            reverse("glossary:import", args=[self.glossary.pk]),
            {"csv_file": upload},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Unknown language code")
        self.assertFalse(Term.objects.filter(glossary=self.glossary, phrase="atom").exists())

    def test_csv_export_neutralizes_spreadsheet_formulas(self):
        Term.objects.create(glossary=self.glossary, phrase="=2+2")
        self.client.force_login(self.teacher)
        response = self.client.get(reverse("glossary:export", args=[self.glossary.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertIn("'=2+2", response.content.decode())

    def test_student_cannot_export_full_glossary(self):
        self.client.force_login(self.student)
        response = self.client.get(reverse("glossary:export", args=[self.glossary.pk]))
        self.assertEqual(response.status_code, 403)

    def test_exam_mode_blocks_unrelated_public_glossary(self):
        public_glossary = Glossary.objects.create(
            creator=self.teacher,
            title="Unrelated public glossary",
            source_language=self.english,
            default_target_language=self.spanish,
            is_public=True,
        )
        self.course.mode = Course.Mode.EXAM
        self.course.save()
        self.client.force_login(self.student)
        response = self.client.get(reverse("glossary:detail", args=[public_glossary.pk]))
        self.assertEqual(response.status_code, 403)

    def test_exam_mode_blocks_another_enrolled_course(self):
        other_course = Course.objects.create(teacher=self.teacher, name="History")
        CourseGlossary.objects.create(course=other_course, glossary=self.glossary)
        Enrollment.objects.create(course=other_course, student=self.student)
        self.course.mode = Course.Mode.EXAM
        self.course.save()
        self.client.force_login(self.student)
        response = self.client.get(
            reverse("glossary:course-view", args=[other_course.pk, self.glossary.pk])
        )
        self.assertEqual(response.status_code, 403)
