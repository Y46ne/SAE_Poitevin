from django.test import TestCase
from django.urls import reverse


class SectionPageTests(TestCase):
    def test_all_public_sections_render(self):
        for name in ("club", "articles", "training", "competition", "partners", "open86"):
            with self.subTest(name=name):
                response = self.client.get(reverse(name))
                self.assertEqual(response.status_code, 200)
