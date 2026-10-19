from django.db import models
from django.db.models import Q
from apps.core.models import MediaAsset, PublishableModel
from apps.competition.models import Player



from .open_edition import OpenEdition

class OpenDraw(models.Model):
    DRAW_CHOICES = (("main", "Tableau final"), ("qualifying", "Qualifications"))
    edition = models.ForeignKey(OpenEdition, on_delete=models.CASCADE, related_name="draws")
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100, blank=True)
    draw_type = models.CharField(max_length=20, choices=DRAW_CHOICES)
    published_file = models.ForeignKey(MediaAsset, null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position", "name"]
        indexes = [models.Index(fields=["edition", "draw_type"])]
