from django.test import TestCase
from django.urls import reverse

from tests.helpers import SYNTHETIC_TEST_CREDENTIAL

from .models import User


class SignupTests(TestCase):
    def test_teacher_can_create_account_with_email(self):
        response = self.client.post(
            reverse("accounts:signup"),
            {
                "email": "teacher@example.test",
                "display_name": "Test Teacher",
                "role": User.Role.TEACHER,
                "password1": SYNTHETIC_TEST_CREDENTIAL,
                "password2": SYNTHETIC_TEST_CREDENTIAL,
            },
        )
        self.assertRedirects(response, reverse("dashboard"))
        user = User.objects.get(email="teacher@example.test")
        self.assertTrue(user.is_teacher)

    def test_email_is_required_and_unique(self):
        User.objects.create_user(email="same@example.test", password=SYNTHETIC_TEST_CREDENTIAL)
        response = self.client.post(
            reverse("accounts:signup"),
            {
                "email": "same@example.test",
                "role": User.Role.STUDENT,
                "password1": SYNTHETIC_TEST_CREDENTIAL,
                "password2": SYNTHETIC_TEST_CREDENTIAL,
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "already exists")

    def test_public_signup_does_not_offer_administrator_role(self):
        response = self.client.get(reverse("accounts:signup"))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, '<option value="admin">', html=False)
