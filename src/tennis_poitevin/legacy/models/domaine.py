"""The Domaine database model."""

from django.db import models
from django.utils import timezone

class Domaine(models.Model):
    nom = models.CharField(max_length=255)
    ordre = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["ordre", "nom"]
