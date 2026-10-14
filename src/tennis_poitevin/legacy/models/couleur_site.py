"""The CouleurSite database model."""

from django.db import models
from django.utils import timezone

class CouleurSite(models.Model):
    nom = models.CharField(max_length=255)
    couleur_primaire = models.CharField(max_length=7)
    couleur_secondaire = models.CharField(max_length=7)
    couleur_action = models.CharField(max_length=7)
    couleur_texte = models.CharField(max_length=7, blank=True, null=True)
    couleur_texte_navbar = models.CharField(max_length=7, blank=True, null=True)
    couleur_texte_bouton = models.CharField(max_length=7, blank=True, null=True)
    couleur_hero = models.CharField(max_length=7, blank=True, null=True)
    couleur_texte_hero = models.CharField(max_length=7, blank=True, null=True)
    couleur_presentation = models.CharField(max_length=7, blank=True, null=True)
    couleur_texte_presentation = models.CharField(max_length=7, blank=True, null=True)
    couleur_slider = models.CharField(max_length=7, blank=True, null=True)
    couleur_texte_slider = models.CharField(max_length=7, blank=True, null=True)
    couleur_partenaire = models.CharField(max_length=7, blank=True, null=True)
    couleur_card = models.CharField(max_length=7, blank=True, null=True)
    couleur_texte_card = models.CharField(max_length=7, blank=True, null=True)
    image_par_defaut = models.CharField(max_length=512, blank=True, null=True)
