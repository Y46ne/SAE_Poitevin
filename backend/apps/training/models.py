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


class TrainingOffer(PublishableModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    audience = models.CharField(max_length=100, blank=True)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position", "name"]
        indexes = [models.Index(fields=["position"]), models.Index(fields=["is_published"])]


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


class Coach(PublishableModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=255, blank=True)
    biography = models.TextField(blank=True)
    photo = models.ForeignKey(MediaAsset, null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    private_lessons = models.BooleanField(default=False)
    offers = models.ManyToManyField(TrainingOffer, blank=True, related_name="coaches")

    class Meta:
        ordering = ["last_name", "first_name"]
        indexes = [models.Index(fields=["last_name"]), models.Index(fields=["is_published"])]
