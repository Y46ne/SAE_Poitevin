from django.db import models
from django.db.models import Q
from apps.training.models import SportsSeason



from .player import Player

class Achievement(models.Model):
    player = models.ForeignKey(Player, on_delete=models.PROTECT, related_name="achievements")
    year = models.PositiveIntegerField()
    competition_name = models.CharField(max_length=255)
    result = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    level = models.CharField(max_length=50, blank=True)
    event = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ["-year", "competition_name"]
        indexes = [models.Index(fields=["year", "level"]), models.Index(fields=["player", "year"])]
