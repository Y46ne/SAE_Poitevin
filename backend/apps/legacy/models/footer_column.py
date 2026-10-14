"""The FooterColumn database model."""

from django.db import models
from django.utils import timezone

from .footer_row import FooterRow

class FooterColumn(models.Model):
    titre = models.CharField(max_length=255, blank=True, null=True)
    ordre = models.IntegerField(default=0)
    row = models.ForeignKey(FooterRow, on_delete=models.CASCADE, related_name="columns")

    class Meta:
        ordering = ["ordre"]
