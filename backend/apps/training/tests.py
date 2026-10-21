from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import SportsSeason, TrainingOffer, TrainingPrice


class TrainingPageTests(TestCase):
    def setUp(self):
        self.season = SportsSeason.objects.create(
            label="2026-2027", starts_on=date(2026, 9, 1), ends_on=date(2027, 8, 31), is_active=True
        )
        self.old_season = SportsSeason.objects.create(
            label="2025-2026", starts_on=date(2025, 9, 1), ends_on=date(2026, 8, 31)
        )

    def test_shows_published_offers_with_active_season_prices(self):
        offer = TrainingOffer.objects.create(
            name="Adhésion Jeune", slug="jeune", audience="Jeunes", is_published=True
        )
        TrainingOffer.objects.create(name="Brouillon", slug="brouillon", is_published=False)
        TrainingPrice.objects.create(offer=offer, season=self.season, label="Classique Jeune", amount=235)
        TrainingPrice.objects.create(offer=offer, season=self.old_season, label="Ancien tarif", amount=200)

        response = self.client.get(reverse("training"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Saison 2026-2027")
        self.assertContains(response, "Adhésion Jeune")
        self.assertContains(response, "Classique Jeune")
        self.assertContains(response, "235&nbsp;€")
        self.assertNotContains(response, "Ancien tarif")
        self.assertNotContains(response, "Brouillon")

    def test_shows_empty_state_without_offers(self):
        response = self.client.get(reverse("training"))

        self.assertContains(response, "Les tarifs de la saison seront bientôt publiés.")

    def test_marks_formation_as_current_page(self):
        response = self.client.get(reverse("training"))

        self.assertContains(response, 'href="/training/" aria-current="page"')
