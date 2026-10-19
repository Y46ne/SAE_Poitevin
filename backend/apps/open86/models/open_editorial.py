from django.db import models
from django.db.models import Q
from apps.core.models import MediaAsset, PublishableModel
from apps.competition.models import Player



from .open_edition import OpenEdition

class OpenEditorial(PublishableModel):
    edition = models.ForeignKey(OpenEdition, on_delete=models.CASCADE, related_name="editorials")
    title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    author_role = models.CharField(max_length=255, blank=True)
    author_photo = models.ForeignKey(MediaAsset, null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    body = models.TextField()
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position", "id"]
        indexes = [models.Index(fields=["edition", "position"]), models.Index(fields=["is_published"])]
