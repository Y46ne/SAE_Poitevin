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
