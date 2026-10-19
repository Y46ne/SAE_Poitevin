from django.db import models
from django.db.models import Q
from apps.core.models import MediaAsset, PublishableModel
from apps.competition.models import Player



from .open_edition import OpenEdition

class OpenPhoto(models.Model):
    edition = models.ForeignKey(OpenEdition, on_delete=models.CASCADE, related_name="photos")
    image = models.ForeignKey(MediaAsset, on_delete=models.PROTECT, related_name="+")
    caption = models.CharField(max_length=255, blank=True)
    alt_text = models.CharField(max_length=255)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position", "id"]
        indexes = [models.Index(fields=["edition", "position"])]
