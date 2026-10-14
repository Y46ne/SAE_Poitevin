"""The NavbarItem database model."""

from django.db import models
from django.utils import timezone

from .navbar import Navbar
from .page import Page

class NavbarItem(models.Model):
    titre = models.CharField(max_length=255)
    type = models.CharField(max_length=255, default="lien")
    route = models.CharField(max_length=255, blank=True, null=True)
    page = models.ForeignKey(Page, on_delete=models.SET_NULL, null=True, blank=True, related_name="navbar_items")
    url_externe = models.CharField(max_length=500, blank=True, null=True)
    navbar = models.ForeignKey(Navbar, on_delete=models.CASCADE, related_name="items")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="enfants")
    ordre = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["ordre"]
