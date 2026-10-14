"""The Media database model."""

from django.db import models
from django.utils import timezone

class Media(models.Model):
    nom = models.CharField(max_length=255)
    fichier = models.CharField(max_length=255)
    type_mime = models.CharField(max_length=100, blank=True, null=True)
    taille = models.IntegerField(blank=True, null=True)
    largeur = models.IntegerField(blank=True, null=True)
    hauteur = models.IntegerField(blank=True, null=True)
    alt = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(default=timezone.now)
    date_modification = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "media"
        ordering = ["-date_creation"]
