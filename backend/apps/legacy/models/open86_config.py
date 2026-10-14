"""The Open86Config database model."""

from django.db import models
from django.utils import timezone

class Open86Config(models.Model):
    est_actif = models.BooleanField(default=False)
    titre = models.CharField(max_length=255, default="Open Masculin 86", blank=True, null=True)
    sous_titre = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    banniere = models.CharField(max_length=500, blank=True, null=True)
    logo = models.CharField(max_length=500, blank=True, null=True)
    date_debut = models.DateTimeField(blank=True, null=True)
    date_fin = models.DateTimeField(blank=True, null=True)
