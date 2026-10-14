"""The Open86FooterRow database model."""

from django.db import models
from django.utils import timezone

from .open86_footer import Open86Footer

class Open86FooterRow(models.Model):
    ordre = models.IntegerField(default=0)
    couleur_fond = models.CharField(max_length=50, blank=True, null=True)
    footer = models.ForeignKey(Open86Footer, on_delete=models.CASCADE, related_name="rows")

    class Meta:
        ordering = ["ordre"]
