"""The Joueur database model."""

from django.db import models
from django.utils import timezone

class Joueur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    classement = models.CharField(max_length=20, blank=True, null=True)
    categorie = models.CharField(max_length=20, blank=True, null=True)
    sexe = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        ordering = ["nom", "prenom"]

    def __str__(self):
        return f"{self.prenom} {self.nom}"
