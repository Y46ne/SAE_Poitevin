from django.db import models
from django.utils import timezone



from .timestamped_model import TimestampedModel

class MediaAsset(TimestampedModel):
    file = models.FileField(upload_to="media/%Y/%m/")
    title = models.CharField(max_length=255, blank=True)
    alt_text = models.CharField(max_length=255, blank=True)
    mime_type = models.CharField(max_length=100, blank=True)
    file_size = models.PositiveBigIntegerField(null=True, blank=True)
    width = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["created_at"])]

    def __str__(self):
        return self.title or self.file.name
