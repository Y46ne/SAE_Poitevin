from django.db import models
from django.db.models import Q
from apps.training.models import SportsSeason



from .team import Team
from .player import Player

class TeamPlayer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")
    player = models.ForeignKey(Player, on_delete=models.PROTECT, related_name="team_memberships")
    season = models.ForeignKey(SportsSeason, on_delete=models.PROTECT, related_name="team_players")

    class Meta:
        ordering = ["team", "player"]
        indexes = [models.Index(fields=["team", "season"])]
        constraints = [models.UniqueConstraint(fields=["team", "player", "season"], name="team_player_season_unique")]
