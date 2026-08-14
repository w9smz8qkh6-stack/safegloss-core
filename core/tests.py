from django.test import TestCase
from django.urls import reverse


class HomeTests(TestCase):
    def test_home_page_describes_public_core(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Create multilingual glossaries")
        self.assertContains(response, "No provider account required")

    def test_health_endpoint(self):
        response = self.client.get(reverse("health"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})
