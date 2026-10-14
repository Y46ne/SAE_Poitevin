"""The Page database model."""

from django.db import models
from django.utils import timezone

from .categorie import Categorie
from .tag import Tag
from .user import User

class Page(models.Model):
    titre = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    est_publie = models.BooleanField(default=False)
    date_modification = models.DateTimeField(default=timezone.now)
    contenu = models.TextField(blank=True, null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True, related_name="pages")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="pages")
    is_draft = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, related_name="pages", blank=True, db_table="page_tag")
    sur_accueil = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date_modification"]
        indexes = [models.Index(fields=["is_draft", "est_publie"])]

    def __str__(self):
        return self.titre
