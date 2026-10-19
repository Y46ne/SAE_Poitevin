from django.db import models
from apps.core.models import MediaAsset, PublishableModel, TimestampedModel



class ClubHistoryEntry(PublishableModel):
    year = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ForeignKey(MediaAsset, null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["year", "position"]
        indexes = [models.Index(fields=["year", "position"]), models.Index(fields=["is_published"])]
