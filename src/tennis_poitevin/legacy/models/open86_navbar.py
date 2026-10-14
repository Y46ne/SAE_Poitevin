"""The Open86Navbar database model."""

from django.db import models
from django.utils import timezone

class Open86Navbar(models.Model):
    nom = models.CharField(max_length=255)
    est_actif = models.BooleanField(default=False)
    logo = models.CharField(max_length=500, blank=True, null=True)
    couleur_fond = models.CharField(max_length=50, blank=True, null=True)
    couleur_texte = models.CharField(max_length=50, blank=True, null=True)
