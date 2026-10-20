from datetime import timedelta

from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIClient

from .models import (
    AdministrativeDocument,
    ClubHistoryEntry,
    ClubProfile,
    ClubStaffMember,
)


class ClubApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.profile = ClubProfile.objects.create(
            name="Stade Poitevin Tennis",
            short_description="Club de tennis à Poitiers",
        )
        self.history = ClubHistoryEntry.objects.create(
            year=1985,
            title="Création du club",
            description="Le club est créé.",
            is_published=True,
        )
        self.staff = ClubStaffMember.objects.create(
            first_name="Alice",
            last_name="Martin",
            role="Présidente",
            is_published=True,
        )
        self.document = AdministrativeDocument.objects.create(
            title="Statuts du club",
            category="Statuts",
            file="club/documents/statuts.pdf",
            is_published=True,
        )

    def test_profile_is_public(self):
        response = self.client.get("/api/v1/club/profile/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["results"][0]["name"], self.profile.name)

    def test_public_club_content_is_returned(self):
        history_response = self.client.get("/api/v1/club/history/")
        management_response = self.client.get("/api/v1/club/management/")
        documents_response = self.client.get("/api/v1/club/documents/")

        self.assertEqual(history_response.data["results"][0]["year"], 1985)
        self.assertEqual(
            management_response.data["results"][0]["role"], "Présidente"
        )
        self.assertEqual(
            documents_response.data["results"][0]["title"], "Statuts du club"
        )

    def test_unpublished_and_future_content_is_hidden(self):
        ClubHistoryEntry.objects.create(
            year=2020,
            title="Brouillon",
            description="Invisible",
        )
        ClubStaffMember.objects.create(
            first_name="Bob",
            last_name="Durand",
            role="Coach",
            is_published=True,
            published_at=timezone.now() + timedelta(days=1),
        )

        history_response = self.client.get("/api/v1/club/history/")
        management_response = self.client.get("/api/v1/club/management/")

        self.assertEqual(history_response.data["count"], 1)
        self.assertEqual(management_response.data["count"], 1)
