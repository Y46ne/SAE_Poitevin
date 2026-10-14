"""The Partenaire database model."""

from django.db import models
from django.utils import timezone

from .domaine import Domaine

class Partenaire(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    domaine = models.ForeignKey(Domaine, on_delete=models.SET_NULL, null=True, blank=True, related_name="partenaires")
    lien = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ["nom"]
