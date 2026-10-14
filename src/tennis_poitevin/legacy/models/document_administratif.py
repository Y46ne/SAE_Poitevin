"""The DocumentAdministratif database model."""

from django.db import models
from django.utils import timezone

class DocumentAdministratif(models.Model):
    titre = models.CharField(max_length=255)
    fichier = models.CharField(max_length=255)
    categorie = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_ajout = models.DateTimeField(default=timezone.now)
    est_actif = models.BooleanField(default=True, null=True)
