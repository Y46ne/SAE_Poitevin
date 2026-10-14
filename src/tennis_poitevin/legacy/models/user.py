"""The User database model."""

from django.db import models
from django.utils import timezone

class User(models.Model):
    email = models.EmailField(max_length=180, unique=True)
    roles = models.JSONField(default=list)
    password = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)

    class Meta:
        db_table = "user"
        ordering = ["nom", "prenom"]

    def __str__(self):
        return f"{self.prenom} {self.nom}".strip()
