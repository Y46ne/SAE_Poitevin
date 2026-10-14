"""The Competition database model."""

from django.db import models
from django.utils import timezone

class Competition(models.Model):
    TYPE_CHAMPIONNAT = "championnat"
    TYPE_TOURNOI = "tournoi"
    nom = models.CharField(max_length=255)
    type = models.CharField(max_length=50, default=TYPE_CHAMPIONNAT)
    categorie = models.CharField(max_length=100, blank=True, null=True)
    division = models.CharField(max_length=50, blank=True, null=True)
    poule = models.CharField(max_length=50, blank=True, null=True)
    annee = models.IntegerField(default=timezone.now().year)
    date_debut = models.DateField(blank=True, null=True)
    date_fin = models.DateField(blank=True, null=True)
    sexe = models.CharField(max_length=20, blank=True, null=True)
    est_actif = models.BooleanField(default=True, null=True)
    classement_final = models.CharField(max_length=50, blank=True, null=True)
    nb_equipes = models.IntegerField(default=0)
    sur_accueil = models.BooleanField(default=False)

    class Meta:
        ordering = ["-annee", "nom"]
        indexes = [models.Index(fields=["annee", "est_actif"])]

    def __str__(self):
        return f"{self.nom} {self.annee}"
