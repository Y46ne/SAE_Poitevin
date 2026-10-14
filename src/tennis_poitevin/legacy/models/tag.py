"""The Tag database model."""

from django.db import models
from django.utils import timezone

class Tag(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100)
    couleur = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        ordering = ["nom"]

    def __str__(self):
        return self.nom
