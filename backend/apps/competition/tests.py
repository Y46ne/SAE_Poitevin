from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.training.models import SportsSeason

from .models import Competition, CompetitionEdition, CompetitionTeam, Match, Team


class MatchValidationTests(TestCase):
    def test_teams_must_belong_to_the_edition(self):
        season = SportsSeason.objects.create(
            label="2026-2027",
            starts_on="2026-09-01",
            ends_on="2027-08-31",
        )
        competition = Competition.objects.create(
            name="Championnat régional",
            slug="championnat-regional",
            competition_type="championship",
        )
        edition = CompetitionEdition.objects.create(competition=competition, season=season)
        home_team = Team.objects.create(name="Équipe A")
        away_team = Team.objects.create(name="Équipe B")
        CompetitionTeam.objects.create(edition=edition, team=home_team)

        with self.assertRaises(ValidationError):
            Match(
                edition=edition,
                home_team=home_team,
                away_team=away_team,
            ).full_clean()
