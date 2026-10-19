from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q
from apps.core.models import MediaAsset, PublishableModel



class TrainingOffer(PublishableModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    audience = models.CharField(max_length=100, blank=True)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position", "name"]
        indexes = [models.Index(fields=["position"]), models.Index(fields=["is_published"])]
