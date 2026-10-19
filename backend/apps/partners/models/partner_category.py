from django.db import models
from django.db.models import Q
from apps.core.models import MediaAsset



class PartnerCategory(models.Model):
    name = models.CharField(max_length=100)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position", "name"]
        indexes = [models.Index(fields=["position"])]
