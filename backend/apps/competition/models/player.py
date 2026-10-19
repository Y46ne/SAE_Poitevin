from django.db import models
from django.db.models import Q
from apps.training.models import SportsSeason



class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=30, blank=True)
    category = models.CharField(max_length=50, blank=True)
    current_ranking = models.CharField(max_length=30, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]
        indexes = [models.Index(fields=["last_name"]), models.Index(fields=["category"])]
