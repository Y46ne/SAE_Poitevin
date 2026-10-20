from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import HomeBlock, HomePage


def home(request):
    now = timezone.now()
    active_blocks = (
        HomeBlock.objects.filter(home_page__is_active=True, is_published=True)
        .filter(Q(published_at__isnull=True) | Q(published_at__lte=now))
        .filter(Q(starts_at__isnull=True) | Q(starts_at__lte=now))
        .filter(Q(ends_at__isnull=True) | Q(ends_at__gte=now))
        .prefetch_related("articles", "competitions", "partners")
    )
    page = get_object_or_404(
        HomePage.objects.filter(is_active=True)
        .prefetch_related("blocks"),
    )
    blocks = active_blocks.filter(home_page=page)
    home_data = {
        "name": page.name,
        "blocks": [
            {
                "id": block.id,
                "type": block.block_type,
                "title": block.title,
                "subtitle": block.subtitle,
                "settings": block.settings,
            }
            for block in blocks
        ],
    }
    return render(request, "home/index.html", {"home_data": home_data})
