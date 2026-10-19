"""The Open86FooterItem database model."""

from django.db import models
from django.utils import timezone

from .open86_footer_column import Open86FooterColumn

class Open86FooterItem(models.Model):
    label = models.CharField(max_length=255)
    url = models.CharField(max_length=500, blank=True, null=True)
    ordre = models.IntegerField(default=0)
    type = models.CharField(max_length=50, default="link")
    icone = models.CharField(max_length=100, blank=True, null=True)
    est_actif = models.BooleanField(default=True)
    column = models.ForeignKey(Open86FooterColumn, on_delete=models.CASCADE, related_name="items", db_column="column_id")

    class Meta:
        ordering = ["ordre"]
