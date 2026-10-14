"""The Navbar database model."""

from django.db import models
from django.utils import timezone

class Navbar(models.Model):
    nom = models.CharField(max_length=255)
    est_active = models.BooleanField(default=False, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
