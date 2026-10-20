from django.db.models import Prefetch, Q
from django.utils import timezone
from rest_framework import viewsets

from .models import Coach, SportsSeason, TrainingOffer, TrainingPrice
from .serializers import (
    CoachSerializer,
    SportsSeasonSerializer,
    TrainingOfferSerializer,
    TrainingPriceSerializer,
)


class PublicTrainingMixin:
    def public_queryset(self, queryset):
        now = timezone.now()
        return queryset.filter(is_published=True).filter(
            Q(published_at__isnull=True) | Q(published_at__lte=now)
        )


class SportsSeasonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SportsSeason.objects.all()
    serializer_class = SportsSeasonSerializer


class TrainingOfferViewSet(PublicTrainingMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = TrainingOfferSerializer

    def get_queryset(self):
        prices = TrainingPrice.objects.select_related("season")
        return self.public_queryset(
            TrainingOffer.objects.prefetch_related(
                Prefetch("prices", queryset=prices),
            )
        )


class TrainingPriceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TrainingPrice.objects.select_related("offer", "season").filter(
        offer__is_published=True
    )
    serializer_class = TrainingPriceSerializer


class CoachViewSet(PublicTrainingMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = CoachSerializer

    def get_queryset(self):
        return self.public_queryset(
            Coach.objects.select_related("photo").prefetch_related("offers")
        )
