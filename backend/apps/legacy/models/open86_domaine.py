"""The Open86Domaine database model."""

from django.db import models
from django.utils import timezone

class Open86Domaine(models.Model):
    nom = models.CharField(max_length=255)
    ordre = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        ordering = ["ordre", "nom"]
