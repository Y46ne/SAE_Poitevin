from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q
from apps.core.models import MediaAsset, PublishableModel



class SportsSeason(models.Model):
    label = models.CharField(max_length=20, unique=True)
    starts_on = models.DateField()
    ends_on = models.DateField()
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ["-starts_on"]
        indexes = [models.Index(fields=["starts_on"]), models.Index(fields=["is_active"])]
        constraints = [
            models.CheckConstraint(condition=Q(ends_on__gte=models.F("starts_on")), name="season_ends_after_start"),
            models.UniqueConstraint(fields=["is_active"], condition=Q(is_active=True), name="one_active_sports_season"),
        ]

    def __str__(self):
        return self.label
