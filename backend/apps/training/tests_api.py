from django.test import TestCase
from rest_framework.test import APIClient

from .models import Coach, SportsSeason, TrainingOffer, TrainingPrice


class TrainingApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.season = SportsSeason.objects.create(
            label="2026-2027", starts_on="2026-09-01", ends_on="2027-06-30", is_active=True
        )
        self.offer = TrainingOffer.objects.create(
            name="École de tennis", slug="ecole-de-tennis", is_published=True
        )
        TrainingPrice.objects.create(
            offer=self.offer, season=self.season, label="Adulte", amount="250.00"
        )
        coach = Coach.objects.create(
            first_name="Jean", last_name="Dupont", role="Entraîneur", is_published=True
        )
        coach.offers.add(self.offer)

    def test_training_endpoints_return_public_data(self):
        offers = self.client.get("/api/v1/training/offers/")
        coaches = self.client.get("/api/v1/training/coaches/")
        prices = self.client.get("/api/v1/training/prices/")

        self.assertEqual(offers.status_code, 200)
        self.assertEqual(offers.data["results"][0]["prices"][0]["label"], "Adulte")
        self.assertEqual(coaches.data["results"][0]["offers"], ["ecole-de-tennis"])
        self.assertEqual(prices.data["results"][0]["amount"], "250.00")
