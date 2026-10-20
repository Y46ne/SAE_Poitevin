from django.test import TestCase
from rest_framework.test import APIClient

from .models import Partner, PartnerCategory


class PartnerApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        category = PartnerCategory.objects.create(name="Principal")
        self.partner = Partner.objects.create(
            name="Entreprise locale", slug="entreprise-locale", category=category
        )

    def test_active_partners_and_categories_are_public(self):
        partners = self.client.get("/api/v1/partners/partners/")
        categories = self.client.get("/api/v1/partners/categories/")

        self.assertEqual(partners.status_code, 200)
        self.assertEqual(partners.data["results"][0]["slug"], self.partner.slug)
        self.assertEqual(categories.data["results"][0]["name"], "Principal")
