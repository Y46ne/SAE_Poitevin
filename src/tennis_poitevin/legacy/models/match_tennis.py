"""The MatchTennis database model."""

from django.db import models
from django.utils import timezone

from .competition import Competition
from .equipe import Equipe

class MatchTennis(models.Model):
    RESULTAT_VICTOIRE = "V"
    RESULTAT_DEFAITE = "D"
    RESULTAT_NUL = "N"
    equipe_domicile = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True, blank=True, related_name="matchs_domicile")
    equipe_exterieur = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True, blank=True, related_name="matchs_exterieur")
    equipe_domicile_club_id = models.IntegerField(blank=True, null=True)
    equipe_exterieur_club_id = models.IntegerField(blank=True, null=True)
    date_match = models.DateField()
    score_domicile = models.CharField(max_length=50, blank=True, null=True)
    score_exterieur = models.CharField(max_length=50, blank=True, null=True)
    resultat = models.CharField(max_length=10, blank=True, null=True)
    est_domicile = models.BooleanField(default=True, null=True)
    lieu = models.CharField(max_length=255, blank=True, null=True)
    commentaire = models.TextField(blank=True, null=True)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, null=True, blank=True, related_name="matchs")
    forfait = models.BooleanField(default=False, null=True)

    class Meta:
        ordering = ["date_match"]
        indexes = [models.Index(fields=["date_match"])]
