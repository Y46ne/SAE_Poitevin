from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q
from apps.core.models import MediaAsset, PublishableModel



from .sports_season import SportsSeason
from .training_offer import TrainingOffer

class TrainingPrice(models.Model):
    offer = models.ForeignKey(TrainingOffer, on_delete=models.CASCADE, related_name="prices")
    season = models.ForeignKey(SportsSeason, on_delete=models.PROTECT, related_name="training_prices")
    label = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])
    currency = models.CharField(max_length=3, default="EUR")
    unit = models.CharField(max_length=50, default="an")
    description = models.TextField(blank=True)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position", "label"]
        indexes = [models.Index(fields=["offer", "season"])]
        constraints = [models.UniqueConstraint(fields=["offer", "season", "label"], name="training_price_offer_season_label_unique")]
