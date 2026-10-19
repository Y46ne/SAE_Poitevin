from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.club.models import ClubProfile
from apps.open86.models import OpenEdition

from .models import Partner, PartnerPlacement


class PartnerPlacementValidationTests(TestCase):
    def test_placement_requires_exactly_one_scope(self):
        partner = Partner.objects.create(name="Partenaire", slug="partenaire")

        with self.assertRaises(ValidationError):
            PartnerPlacement(partner=partner).full_clean()

        club = ClubProfile.objects.create(name="Stade Poitevin Tennis")
        edition = OpenEdition.objects.create(year=2026)
        with self.assertRaises(ValidationError):
            PartnerPlacement(
                partner=partner,
                club=club,
                open_edition=edition,
            ).full_clean()
