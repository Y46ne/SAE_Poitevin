from django.test import TestCase
from rest_framework.test import APIClient

from apps.training.models import SportsSeason

from .models import Competition, CompetitionEdition, Match, Team


class CompetitionApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        season = SportsSeason.objects.create(
            label="2026-2027", starts_on="2026-09-01", ends_on="2027-06-30"
        )
        competition = Competition.objects.create(
            name="Championnat régional", slug="championnat-regional", competition_type="championship"
        )
        edition = CompetitionEdition.objects.create(competition=competition, season=season)
        home = Team.objects.create(name="Stade Poitevin", is_club_team=True)
        away = Team.objects.create(name="Club visiteur")
        edition.teams.create(team=home)
        edition.teams.create(team=away)
        Match.objects.create(edition=edition, home_team=home, away_team=away, status="scheduled")

    def test_competitions_editions_and_matches_are_public(self):
        competitions = self.client.get("/api/v1/competition/competitions/")
        editions = self.client.get("/api/v1/competition/editions/")
        matches = self.client.get("/api/v1/competition/matches/")

        self.assertEqual(competitions.data["results"][0]["slug"], "championnat-regional")
        self.assertEqual(editions.data["results"][0]["competition"]["name"], "Championnat régional")
        self.assertEqual(matches.data["results"][0]["home_team"]["name"], "Stade Poitevin")
