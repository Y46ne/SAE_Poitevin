from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import HomePage


def home(request):
    page = get_object_or_404(HomePage, is_active=True)
    now = timezone.now()
    blocks = (
        page.blocks.filter(is_published=True)
        .filter(Q(published_at__isnull=True) | Q(published_at__lte=now))
        .filter(Q(starts_at__isnull=True) | Q(starts_at__lte=now))
        .filter(Q(ends_at__isnull=True) | Q(ends_at__gte=now))
    )
    return render(request, "home/index.html", {"page": page, "blocks": blocks})
