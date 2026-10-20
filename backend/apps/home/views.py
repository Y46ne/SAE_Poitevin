from django.db.models import Prefetch, Q
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.generics import RetrieveAPIView

from apps.competition.models import Competition
from apps.content.models import Article
from apps.partners.models import Partner

from .models import HomeBlock, HomePage
from .serializers import HomePageSerializer


class HomePageView(RetrieveAPIView):
    serializer_class = HomePageSerializer

    def get_object(self):
        now = timezone.now()
        public_articles = Article.objects.filter(is_published=True).filter(
            Q(published_at__isnull=True) | Q(published_at__lte=now)
        )
        active_blocks = HomeBlock.objects.filter(is_published=True).filter(
            Q(published_at__isnull=True) | Q(published_at__lte=now)
        ).filter(
            Q(starts_at__isnull=True) | Q(starts_at__lte=now)
        ).filter(
            Q(ends_at__isnull=True) | Q(ends_at__gte=now)
        ).select_related("home_page").prefetch_related(
            Prefetch(
                "articles",
                queryset=public_articles.select_related("cover", "category"),
            ),
            "competitions",
            "partners",
        )
        pages = HomePage.objects.filter(is_active=True).prefetch_related(
            Prefetch("blocks", queryset=active_blocks)
        ).order_by("id")
        return get_object_or_404(pages)
