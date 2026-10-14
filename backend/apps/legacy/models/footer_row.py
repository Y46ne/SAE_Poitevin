"""The FooterRow database model."""

from django.db import models
from django.utils import timezone

from .footer import Footer

class FooterRow(models.Model):
    background_color = models.CharField(max_length=50, blank=True, null=True)
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE, related_name="rows")
    ordre = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["ordre"]
