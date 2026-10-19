"""The MembreManagement database model."""

from django.db import models
from django.utils import timezone

class MembreManagement(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    fonction = models.CharField(max_length=255)
    photo = models.CharField(max_length=255, blank=True, null=True)
    biographie = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    est_actif = models.BooleanField(default=True, null=True)

    class Meta:
        ordering = ["nom", "prenom"]
