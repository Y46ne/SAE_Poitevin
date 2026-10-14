"""The Footer database model."""

from django.db import models
from django.utils import timezone

class Footer(models.Model):
    nom = models.CharField(max_length=255)
    est_actif = models.BooleanField(default=False)
    copyright = models.CharField(max_length=255, blank=True, null=True)
