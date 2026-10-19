from django.db import models
from apps.core.models import MediaAsset, PublishableModel, TimestampedModel



class ClubProfile(TimestampedModel):
    name = models.CharField(max_length=255)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    address = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["name"])]
        verbose_name = "Fiche du club"
        verbose_name_plural = "Fiche du club"

    def __str__(self):
        return self.name
