"""The CoursFormation database model."""

from django.db import models
from django.utils import timezone

class CoursFormation(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    position = models.IntegerField(default=0)
    est_actif = models.BooleanField(default=True, null=True)

    class Meta:
        ordering = ["position"]
