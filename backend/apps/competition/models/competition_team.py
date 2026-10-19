from django.db import models
from django.db.models import Q
from apps.training.models import SportsSeason



from .competition_edition import CompetitionEdition
from .team import Team

class CompetitionTeam(models.Model):
    edition = models.ForeignKey(CompetitionEdition, on_delete=models.CASCADE, related_name="teams")
    team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="competition_memberships")

    class Meta:
        ordering = ["edition", "team"]
        indexes = [models.Index(fields=["edition", "team"])]
        constraints = [models.UniqueConstraint(fields=["edition", "team"], name="competition_team_unique")]
