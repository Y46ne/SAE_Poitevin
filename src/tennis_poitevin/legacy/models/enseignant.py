"""The Enseignant database model."""

from django.db import models
from django.utils import timezone

class Enseignant(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    diplome = models.CharField(max_length=255)
    fonction = models.CharField(max_length=255, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    biographie = models.TextField(blank=True, null=True)
    est_actif = models.BooleanField(default=True, null=True)
    cours_particuliers = models.BooleanField(default=False, null=True)

    class Meta:
        ordering = ["nom", "prenom"]
