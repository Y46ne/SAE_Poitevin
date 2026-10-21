from django.db.models import Prefetch, Q
from django.shortcuts import render
from django.utils import timezone

from .models import Coach, SportsSeason, TrainingOffer, TrainingPrice


def _published(queryset):
    now = timezone.now()
    return queryset.filter(is_published=True).filter(
        Q(published_at__isnull=True) | Q(published_at__lte=now)
    )


def training(request):
    season = SportsSeason.objects.filter(is_active=True).first()
    prices = TrainingPrice.objects.filter(season=season)
    offers = (
        _published(TrainingOffer.objects.all())
        .select_related("cover")
        .prefetch_related(Prefetch("prices", queryset=prices))
    )
    coaches = _published(Coach.objects.all()).select_related("photo")
    return render(
        request,
        "training/index.html",
        {"season": season, "offers": offers, "coaches": coaches},
    )
