from django.apps import AppConfig


class LegacyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.legacy"
    # Keep the historical app label so existing database tables and migrations
    # remain attached to the same Django application.
    label = "legacy"
    verbose_name = "Modele du site historique"
