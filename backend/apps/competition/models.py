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


class CompetitionEdition(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name="editions")
    season = models.ForeignKey(SportsSeason, on_delete=models.PROTECT, related_name="competition_editions")
    category = models.CharField(max_length=100, blank=True)
    division = models.CharField(max_length=100, blank=True)
    group = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=30, blank=True)
    starts_on = models.DateField(null=True, blank=True)
    ends_on = models.DateField(null=True, blank=True)
    final_ranking = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-season__starts_on", "competition__name"]
        indexes = [models.Index(fields=["season", "is_active"]), models.Index(fields=["starts_on"])]
        constraints = [models.CheckConstraint(condition=Q(ends_on__isnull=True) | Q(starts_on__isnull=True) | Q(ends_on__gte=models.F("starts_on")), name="competition_edition_ends_after_start")]


class Team(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100, blank=True)
    is_club_team = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["name"]), models.Index(fields=["is_club_team"])]

    def __str__(self):
        return self.name


class CompetitionTeam(models.Model):
    edition = models.ForeignKey(CompetitionEdition, on_delete=models.CASCADE, related_name="teams")
    team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="competition_memberships")

    class Meta:
        ordering = ["edition", "team"]
        indexes = [models.Index(fields=["edition", "team"])]
        constraints = [models.UniqueConstraint(fields=["edition", "team"], name="competition_team_unique")]


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


class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=30, blank=True)
    category = models.CharField(max_length=50, blank=True)
    current_ranking = models.CharField(max_length=30, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]
        indexes = [models.Index(fields=["last_name"]), models.Index(fields=["category"])]


class TeamPlayer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")
    player = models.ForeignKey(Player, on_delete=models.PROTECT, related_name="team_memberships")
    season = models.ForeignKey(SportsSeason, on_delete=models.PROTECT, related_name="team_players")

    class Meta:
        ordering = ["team", "player"]
        indexes = [models.Index(fields=["team", "season"])]
        constraints = [models.UniqueConstraint(fields=["team", "player", "season"], name="team_player_season_unique")]


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
