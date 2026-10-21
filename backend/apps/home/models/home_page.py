from django.db import models
from django.db.models import Q
from apps.core.models import MediaAsset, PublishableModel, TimestampedModel



class HomePage(TimestampedModel):
    name = models.CharField(max_length=100, default="Accueil")
    cover = models.ForeignKey(MediaAsset, null=True, blank=True, on_delete=models.SET_NULL, related_name="+", verbose_name="photo du bandeau")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["is_active"])]
        constraints = [models.UniqueConstraint(fields=["is_active"], condition=Q(is_active=True), name="one_active_home_page")]
