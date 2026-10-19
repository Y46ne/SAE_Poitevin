from django.db import models
from django.db.models import Q
from apps.training.models import SportsSeason



from .competition_edition import CompetitionEdition
from .team import Team
from .competition_team import CompetitionTeam

class Match(models.Model):
    STATUS_CHOICES = (("scheduled", "Programmé"), ("played", "Joué"), ("cancelled", "Annulé"))
    edition = models.ForeignKey(CompetitionEdition, on_delete=models.CASCADE, related_name="matches")
    home_team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="home_matches")
    away_team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="away_matches")
    scheduled_at = models.DateTimeField(null=True, blank=True)
    venue = models.CharField(max_length=255, blank=True)
    home_score = models.PositiveIntegerField(null=True, blank=True)
    away_score = models.PositiveIntegerField(null=True, blank=True)
    score_detail = models.JSONField(default=list, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="scheduled")
    is_forfeit = models.BooleanField(default=False)
    comment = models.TextField(blank=True)

    class Meta:
        ordering = ["scheduled_at", "id"]
        indexes = [models.Index(fields=["edition", "scheduled_at"]), models.Index(fields=["status"])]
        constraints = [models.CheckConstraint(condition=~Q(home_team=models.F("away_team")), name="match_teams_are_different")]

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.home_team_id == self.away_team_id:
            raise ValidationError("Une rencontre doit opposer deux équipes différentes.")
        if self.edition_id:
            team_ids = set(
                CompetitionTeam.objects.filter(edition_id=self.edition_id).values_list(
                    "team_id", flat=True
                )
            )
            if {self.home_team_id, self.away_team_id} - team_ids:
                raise ValidationError(
                    "Les deux équipes doivent participer à l'édition de la compétition."
                )
