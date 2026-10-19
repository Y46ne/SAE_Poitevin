from django.db import models
from django.db.models import Q
from apps.core.models import MediaAsset, PublishableModel
from apps.competition.models import Player



class OpenEdition(PublishableModel):
    year = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=255, default="Open Masculin 86")
    subtitle = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    logo = models.ForeignKey(MediaAsset, null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    banner = models.ForeignKey(MediaAsset, null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    starts_at = models.DateTimeField(null=True, blank=True)
    ends_at = models.DateTimeField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)

    class Meta:
        ordering = ["-year"]
        indexes = [models.Index(fields=["is_published", "-year"]), models.Index(fields=["is_current"])]
        constraints = [
            models.UniqueConstraint(fields=["is_current"], condition=Q(is_current=True), name="one_current_open_edition"),
            models.CheckConstraint(condition=Q(ends_at__isnull=True) | Q(starts_at__isnull=True) | Q(ends_at__gte=models.F("starts_at")), name="open_edition_ends_after_start"),
        ]
