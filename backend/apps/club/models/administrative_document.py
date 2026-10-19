from django.db import models
from apps.core.models import MediaAsset, PublishableModel, TimestampedModel



class AdministrativeDocument(PublishableModel):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    file = models.FileField(upload_to="club/documents/%Y/")
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["-published_at", "title"]
        indexes = [models.Index(fields=["category"]), models.Index(fields=["is_published", "-published_at"])]
