"""The Open86Edito database model."""

from django.db import models
from django.utils import timezone

class Open86Edito(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    fonction = models.CharField(max_length=255)
    photo = models.CharField(max_length=255, blank=True, null=True)
    contenu = models.TextField(blank=True, null=True)
    ordre = models.IntegerField(default=0, blank=True, null=True)
    est_actif = models.BooleanField(default=True, null=True)

    class Meta:
        ordering = ["ordre"]
