from django.db import models
from django.db.models import Q
from apps.training.models import SportsSeason



class Team(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100, blank=True)
    is_club_team = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["name"]), models.Index(fields=["is_club_team"])]

    def __str__(self):
        return self.name
