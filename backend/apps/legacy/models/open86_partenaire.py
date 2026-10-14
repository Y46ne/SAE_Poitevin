"""The Open86Partenaire database model."""

from django.db import models
from django.utils import timezone

from .open86_domaine import Open86Domaine

class Open86Partenaire(models.Model):
    nom = models.CharField(max_length=255)
    logo = models.CharField(max_length=255, blank=True, null=True)
    domaine = models.ForeignKey(Open86Domaine, on_delete=models.SET_NULL, null=True, blank=True, related_name="partenaires")
    lien = models.CharField(max_length=255, blank=True, null=True)
