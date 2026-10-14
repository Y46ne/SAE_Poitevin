"""The HistoireClub database model."""

from django.db import models
from django.utils import timezone

from .page import Page

class HistoireClub(models.Model):
    annee = models.IntegerField()
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255, blank=True, null=True)
    est_actif = models.BooleanField(default=True, null=True)
    page = models.ForeignKey(Page, on_delete=models.SET_NULL, null=True, blank=True, related_name="histoires")

    class Meta:
        ordering = ["annee"]
