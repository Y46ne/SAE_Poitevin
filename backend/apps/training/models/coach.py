from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q
from apps.core.models import MediaAsset, PublishableModel



from .training_offer import TrainingOffer

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
