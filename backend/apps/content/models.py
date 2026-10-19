from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from apps.core.models import MediaAsset, PublishableModel


class ArticleCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["name"])]

    def __str__(self):
        return self.name


class ArticleTag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["name"])]

    def __str__(self):
        return self.name


class Article(PublishableModel):
    SCOPE_CLUB = "club"
    SCOPE_OPEN = "open86"
    SCOPE_CHOICES = ((SCOPE_CLUB, "Club"), (SCOPE_OPEN, "Open 86"))
    scope = models.CharField(max_length=10, choices=SCOPE_CHOICES)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    excerpt = models.TextField(blank=True)
    body = models.TextField()
    cover = models.ForeignKey(MediaAsset, null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="articles")
    category = models.ForeignKey(ArticleCategory, null=True, blank=True, on_delete=models.SET_NULL, related_name="articles")
    tags = models.ManyToManyField(ArticleTag, blank=True, related_name="articles")
    open_edition = models.ForeignKey("open86.OpenEdition", null=True, blank=True, on_delete=models.CASCADE, related_name="articles")

    class Meta:
        ordering = ["-published_at", "-created_at"]
        indexes = [models.Index(fields=["scope", "is_published", "-published_at"])]
        constraints = [
            models.UniqueConstraint(fields=["scope", "slug"], condition=Q(scope="club"), name="club_article_scope_slug_unique"),
            models.UniqueConstraint(fields=["scope", "slug", "open_edition"], condition=Q(scope="open86"), name="open_article_scope_slug_edition_unique"),
            models.CheckConstraint(condition=Q(scope="club", open_edition__isnull=True) | Q(scope="open86", open_edition__isnull=False), name="article_scope_matches_edition"),
        ]

    def clean(self):
        if self.scope == self.SCOPE_CLUB and self.open_edition_id:
            raise ValidationError("Un article du club ne peut pas avoir d'édition Open.")
        if self.scope == self.SCOPE_OPEN and not self.open_edition_id:
            raise ValidationError("Un article Open doit être rattaché à une édition.")

    def __str__(self):
        return self.title
