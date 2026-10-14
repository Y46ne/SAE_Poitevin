"""The Open86SectionAccueil database model."""

from django.db import models
from django.utils import timezone

class Open86SectionAccueil(models.Model):
    titre = models.CharField(max_length=255)
    type = models.CharField(max_length=100, default="texte")
    contenu = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=500, blank=True, null=True)
    lien_bouton = models.CharField(max_length=500, blank=True, null=True)
    texte_bouton = models.CharField(max_length=100, blank=True, null=True)
    ordre = models.IntegerField(default=0)
    est_actif = models.BooleanField(default=True)
    couleur_fond = models.CharField(max_length=50, blank=True, null=True)
    couleur_texte = models.CharField(max_length=50, blank=True, null=True)
    options = models.JSONField(blank=True, null=True)
    partenaire_images = models.JSONField(blank=True, null=True)

    class Meta:
        ordering = ["ordre"]
