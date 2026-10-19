from django.db import models
from django.db.models import Q
from apps.training.models import SportsSeason



from .competition import Competition

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
