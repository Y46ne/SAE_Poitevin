from django.db import models
from django.db.models import Q
from apps.core.models import MediaAsset, PublishableModel
from apps.competition.models import Player



from .open_edition import OpenEdition

class OpenProgramItem(models.Model):
    edition = models.ForeignKey(OpenEdition, on_delete=models.CASCADE, related_name="program_items")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=100, blank=True)
    is_published = models.BooleanField(default=True)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["starts_at", "position"]
        indexes = [models.Index(fields=["edition", "starts_at", "is_published"])]
        constraints = [models.CheckConstraint(condition=Q(ends_at__isnull=True) | Q(ends_at__gte=models.F("starts_at")), name="open_program_ends_after_start")]
