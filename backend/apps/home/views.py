from django.db.models import Prefetch, Q
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from apps.club.models import ClubProfile
from apps.content.models import Article
from apps.open86.models import OpenEdition
from apps.partners.models import Partner

from .models import HomePage


def _published(queryset, now):
    return queryset.filter(is_published=True).filter(
        Q(published_at__isnull=True) | Q(published_at__lte=now)
    )


def home(request):
    page = get_object_or_404(HomePage.objects.select_related("cover"), is_active=True)
    now = timezone.now()
    articles = _published(Article.objects.all(), now).select_related("cover", "category")
    blocks = list(
        _published(page.blocks.all(), now)
        .filter(Q(starts_at__isnull=True) | Q(starts_at__lte=now))
        .filter(Q(ends_at__isnull=True) | Q(ends_at__gte=now))
        .prefetch_related(Prefetch("articles", queryset=articles))
    )
    context = {
        "page": page,
        "club": ClubProfile.objects.first(),
        "figures": [block for block in blocks if block.figure],
        "featured": [block for block in blocks if not block.figure],
        "open_edition": _published(OpenEdition.objects.filter(is_current=True), now)
        .select_related("banner")
        .first(),
        "partners": Partner.objects.filter(is_active=True, logo__isnull=False).select_related("logo"),
    }
    return render(request, "home/index.html", context)
