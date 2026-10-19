"""The Open86Footer database model."""

from django.db import models
from django.utils import timezone

class Open86Footer(models.Model):
    nom = models.CharField(max_length=255)
    est_actif = models.BooleanField(default=False)
    couleur_fond = models.CharField(max_length=50, blank=True, null=True)
    couleur_texte = models.CharField(max_length=50, blank=True, null=True)
    copyright = models.TextField(blank=True, null=True)
