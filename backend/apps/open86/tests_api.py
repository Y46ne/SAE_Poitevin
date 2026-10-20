from django.test import TestCase
from rest_framework.test import APIClient

from .models import OpenEdition, OpenPhoto, OpenProgramItem


class OpenApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.edition = OpenEdition.objects.create(
            year=2026, title="Open Masculin 86 2026", is_published=True, is_current=True
        )
        OpenProgramItem.objects.create(
            edition=self.edition,
            title="Finale",
            starts_at="2026-10-20T14:00:00Z",
            is_published=True,
        )

    def test_public_edition_and_program_are_returned(self):
        editions = self.client.get("/api/v1/open86/editions/")
        program = self.client.get("/api/v1/open86/program/")

        self.assertEqual(editions.data["results"][0]["year"], 2026)
        self.assertEqual(program.data["results"][0]["title"], "Finale")

    def test_archived_or_draft_edition_is_hidden(self):
        OpenEdition.objects.create(year=2025, title="Ancienne édition", is_archived=True)

        response = self.client.get("/api/v1/open86/editions/")

        self.assertEqual(response.data["count"], 1)
