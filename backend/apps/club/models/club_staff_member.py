from django.db import models
from apps.core.models import MediaAsset, PublishableModel, TimestampedModel



class ClubStaffMember(PublishableModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=255)
    biography = models.TextField(blank=True)
    photo = models.ForeignKey(MediaAsset, null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position", "last_name", "first_name"]
        indexes = [models.Index(fields=["position"]), models.Index(fields=["is_published"])]
