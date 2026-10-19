"""The Open86FooterColumn database model."""

from django.db import models
from django.utils import timezone

from .open86_footer_row import Open86FooterRow

class Open86FooterColumn(models.Model):
    titre = models.CharField(max_length=255, blank=True, null=True)
    ordre = models.IntegerField(default=0)
    largeur = models.IntegerField(default=3)
    row = models.ForeignKey(Open86FooterRow, on_delete=models.CASCADE, related_name="columns")

    class Meta:
        ordering = ["ordre"]
