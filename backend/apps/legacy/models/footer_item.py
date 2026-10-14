"""The FooterItem database model."""

from django.db import models
from django.utils import timezone

from .footer_column import FooterColumn
from .page import Page

class FooterItem(models.Model):
    TYPE_TEXT = "text"
    TYPE_LINK = "link"
    TYPE_SOCIAL = "social"
    type = models.CharField(max_length=50, default=TYPE_TEXT)
    contenu = models.CharField(max_length=255)
    url = models.CharField(max_length=500, blank=True, null=True)
    page = models.ForeignKey(Page, on_delete=models.SET_NULL, null=True, blank=True, related_name="footer_items")
    route = models.CharField(max_length=255, blank=True, null=True)
    icone = models.CharField(max_length=50, blank=True, null=True)
    ordre = models.IntegerField(default=0)
    column = models.ForeignKey(FooterColumn, on_delete=models.CASCADE, related_name="items")

    class Meta:
        ordering = ["ordre"]
