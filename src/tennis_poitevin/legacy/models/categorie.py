"""The Categorie database model."""

from django.db import models
from django.utils import timezone

class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    slug = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["nom"]

    def __str__(self):
        return self.nom
