"""The Palmares database model."""

from django.db import models
from django.utils import timezone

from .joueur import Joueur

class Palmares(models.Model):
    TYPE_VAINQUEUR = "Vainqueur"
    TYPE_FINALISTE = "Finaliste"
    TYPE_DEMI_FINALISTE = "Demi-finaliste"
    TYPE_QUART_FINALISTE = "Quart de finaliste"
    NIVEAU_DEPARTEMENTAL = "Départemental"
    NIVEAU_REGIONAL = "Régional"
    NIVEAU_NATIONAL = "National"
    NIVEAU_INTERNATIONAL = "International"
    joueur = models.ForeignKey(Joueur, on_delete=models.CASCADE, related_name="palmares")
    annee = models.IntegerField()
    competition = models.CharField(max_length=255)
    resultat = models.CharField(max_length=100, default=TYPE_VAINQUEUR)
    categorie = models.CharField(max_length=100, blank=True, null=True)
    niveau = models.CharField(max_length=50, default=NIVEAU_DEPARTEMENTAL, blank=True, null=True)
    epreuve = models.CharField(max_length=50, blank=True, null=True)
    est_actif = models.BooleanField(default=True, null=True)

    class Meta:
        ordering = ["-annee", "competition"]
