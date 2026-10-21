from django.db import models
from django.db.models import Q
from apps.core.models import PublishableModel, TimestampedModel



from .home_page import HomePage

class HomeBlock(PublishableModel):
    TYPE_RENCONTRE = "rencontre"
    TYPE_TOURNOI = "tournoi"
    TYPE_INFO = "info"
    TYPE_GALERIE = "galerie"
    TYPE_CHOICES = (
        (TYPE_RENCONTRE, "Rencontre"),
        (TYPE_TOURNOI, "Tournoi"),
        (TYPE_INFO, "Information"),
        (TYPE_GALERIE, "Galerie"),
    )
    home_page = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name="blocks")
    block_type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    title = models.CharField(max_length=255, blank=True)
    subtitle = models.TextField(blank=True)
    position = models.PositiveIntegerField(default=0)
    starts_at = models.DateTimeField(null=True, blank=True)
    ends_at = models.DateTimeField(null=True, blank=True)
    settings = models.JSONField(default=dict, blank=True)
    articles = models.ManyToManyField("content.Article", blank=True, related_name="home_blocks")
    competitions = models.ManyToManyField("competition.Competition", blank=True, related_name="home_blocks")
    partners = models.ManyToManyField("partners.Partner", blank=True, related_name="home_blocks")

    class Meta:
        ordering = ["position", "id"]
        indexes = [models.Index(fields=["home_page", "position"]), models.Index(fields=["is_published"])]
        constraints = [
            models.UniqueConstraint(fields=["home_page", "position"], name="home_block_position_unique"),
            models.CheckConstraint(condition=Q(ends_at__isnull=True) | Q(starts_at__isnull=True) | Q(ends_at__gte=models.F("starts_at")), name="home_block_ends_after_start"),
        ]

    @property
    def figure(self):
        """Chiffre clé d'un bloc « Information », saisi dans settings : {"value": "9"}."""
        if self.block_type == self.TYPE_INFO and isinstance(self.settings, dict):
            return str(self.settings.get("value", ""))
        return ""
