from django.db import models
from django.db.models import Q
from apps.training.models import SportsSeason



class Competition(models.Model):
    TYPE_CHOICES = (("championship", "Championnat"), ("tournament", "Tournoi"), ("internal", "Interne"))
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    competition_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["competition_type"])]
