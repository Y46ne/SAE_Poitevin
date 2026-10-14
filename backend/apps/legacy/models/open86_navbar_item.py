"""The Open86NavbarItem database model."""

from django.db import models
from django.utils import timezone

from .open86_navbar import Open86Navbar

class Open86NavbarItem(models.Model):
    label = models.CharField(max_length=255)
    url = models.CharField(max_length=500, blank=True, null=True)
    ordre = models.IntegerField(default=0)
    type = models.CharField(max_length=50, default="link", blank=True, null=True)
    icone = models.CharField(max_length=100, blank=True, null=True)
    est_actif = models.BooleanField(default=True)
    navbar = models.ForeignKey(Open86Navbar, on_delete=models.CASCADE, related_name="items")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    class Meta:
        ordering = ["ordre"]
