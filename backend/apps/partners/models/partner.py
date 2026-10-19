from django.db import models
from django.db.models import Q
from apps.core.models import MediaAsset



from .partner_category import PartnerCategory

class Partner(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    logo = models.ForeignKey(MediaAsset, null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(PartnerCategory, null=True, blank=True, on_delete=models.SET_NULL, related_name="partners")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["is_active"]), models.Index(fields=["category", "is_active"])]
