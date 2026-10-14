"""The Equipe database model."""

from django.db import models
from django.utils import timezone

from .competition import Competition

class Equipe(models.Model):
    nom = models.CharField(max_length=255)
    ville = models.CharField(max_length=100, blank=True, null=True)
    est_club = models.BooleanField(default=False, null=True)
    competitions = models.ManyToManyField(Competition, related_name="equipes", blank=True)

    class Meta:
        ordering = ["nom"]

    def __str__(self):
        return self.nom
