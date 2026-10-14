"""The SectionAccueil database model."""

from django.db import models
from django.utils import timezone

from .categorie import Categorie

class SectionAccueil(models.Model):
    TYPE_HERO = "hero"
    TYPE_PRESENTATION = "presentation"
    TYPE_CUSTOM = "custom"
    TYPE_SLIDER = "slider"
    TYPE_PARTENAIRE = "partenaire"
    TYPE_MATCH = "match"
    titre = models.CharField(max_length=255)
    contenu = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    position = models.IntegerField(default=0)
    est_actif = models.BooleanField(default=True, null=True)
    type = models.CharField(max_length=50, default="texte")
    slider_mode = models.CharField(max_length=20, blank=True, null=True)
    slider_images = models.JSONField(blank=True, null=True)
    slider_categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True, related_name="sections_slider")
    slider_bouton_texte = models.CharField(max_length=255, blank=True, null=True)
    slider_bouton_url = models.CharField(max_length=255, blank=True, null=True)
    slider_nb_cards = models.SmallIntegerField(default=3, blank=True, null=True)
    slider_show_arrows = models.BooleanField(default=False, blank=True, null=True)
    partenaire_images = models.JSONField(blank=True, null=True)

    class Meta:
        ordering = ["position"]
