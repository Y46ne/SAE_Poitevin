from django.db.models import Q
from django.utils import timezone
from rest_framework import filters, viewsets

from .models import Article, ArticleCategory, ArticleTag
from .serializers import (
    ArticleCategorySerializer,
    ArticleDetailSerializer,
    ArticleListSerializer,
    ArticleTagSerializer,
)


class PublicArticleQuerysetMixin:
    def public_queryset(self, queryset):
        now = timezone.now()
        return queryset.filter(is_published=True).filter(
            Q(published_at__isnull=True) | Q(published_at__lte=now)
        )


class ArticleViewSet(PublicArticleQuerysetMixin, viewsets.ReadOnlyModelViewSet):
    lookup_field = "slug"
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("title", "excerpt", "body")
    ordering_fields = ("published_at", "title")
    ordering = ("-published_at", "-created_at")

    def get_queryset(self):
        queryset = Article.objects.select_related("cover", "category").prefetch_related("tags")
        queryset = self.public_queryset(queryset)
        scope = self.request.query_params.get("scope")
        category = self.request.query_params.get("category")
        tag = self.request.query_params.get("tag")
        if scope:
            queryset = queryset.filter(scope=scope)
        if category:
            queryset = queryset.filter(category__slug=category)
        if tag:
            queryset = queryset.filter(tags__slug=tag)
        return queryset.distinct()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ArticleDetailSerializer
        return ArticleListSerializer


class ArticleCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategorySerializer
    lookup_field = "slug"
    pagination_class = None


class ArticleTagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ArticleTag.objects.all()
    serializer_class = ArticleTagSerializer
    lookup_field = "slug"
    pagination_class = None
