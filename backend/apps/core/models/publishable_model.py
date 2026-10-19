from django.db import models
from django.utils import timezone



from .timestamped_model import TimestampedModel

class PublishableModel(TimestampedModel):
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    @property
    def is_public(self):
        return self.is_published and (
            self.published_at is None or self.published_at <= timezone.now()
        )
