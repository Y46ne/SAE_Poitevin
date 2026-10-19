from django.db import models
from apps.core.models import MediaAsset, PublishableModel, TimestampedModel


class ClubProfile(TimestampedModel):
    name = models.CharField(max_length=255)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    address = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["name"])]
        verbose_name = "Fiche du club"
        verbose_name_plural = "Fiche du club"

    def __str__(self):
        return self.name


class ClubHistoryEntry(PublishableModel):
    year = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ForeignKey(MediaAsset, null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["year", "position"]
        indexes = [models.Index(fields=["year", "position"]), models.Index(fields=["is_published"])]


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


class AdministrativeDocument(PublishableModel):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    file = models.FileField(upload_to="club/documents/%Y/")
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["-published_at", "title"]
        indexes = [models.Index(fields=["category"]), models.Index(fields=["is_published", "-published_at"])]
