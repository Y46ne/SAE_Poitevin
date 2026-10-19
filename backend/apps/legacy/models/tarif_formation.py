"""The TarifFormation database model."""

from django.db import models
from django.utils import timezone

from .cours_formation import CoursFormation

class TarifFormation(models.Model):
    intitule = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    unite = models.CharField(max_length=50, default="an", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    position = models.IntegerField(default=0)
    cours_formation = models.ForeignKey(CoursFormation, on_delete=models.CASCADE, related_name="tarifs")

    class Meta:
        ordering = ["position"]
