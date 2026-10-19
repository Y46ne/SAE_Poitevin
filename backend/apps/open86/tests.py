from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.competition.models import Player

from .models import OpenDraw, OpenDrawMatch, OpenEdition


class OpenDrawMatchValidationTests(TestCase):
    def test_winner_must_be_one_of_the_players(self):
        edition = OpenEdition.objects.create(year=2026, title="Open Masculin 86 2026")
        draw = OpenDraw.objects.create(
            edition=edition,
            name="Tableau final",
            draw_type="main",
        )
        player_one = Player.objects.create(first_name="A", last_name="Joueur")
        player_two = Player.objects.create(first_name="B", last_name="Joueur")
        outsider = Player.objects.create(first_name="C", last_name="Joueur")

        with self.assertRaises(ValidationError):
            OpenDrawMatch(
                draw=draw,
                round_name="Finale",
                player_one=player_one,
                player_two=player_two,
                winner=outsider,
            ).full_clean()
