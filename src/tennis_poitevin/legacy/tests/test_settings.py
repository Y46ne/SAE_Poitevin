from importlib import import_module

from django.conf import settings
from django.test import SimpleTestCase


class DevelopmentSettingsTests(SimpleTestCase):
    """Protect the defaults used by the local development entry point."""

    def test_development_settings_keep_local_defaults(self):
        development_settings = import_module(settings.SETTINGS_MODULE)
        self.assertTrue(development_settings.DEBUG)
        self.assertEqual(development_settings.ALLOWED_HOSTS, [])
        self.assertEqual(
            settings.DATABASES["default"]["ENGINE"],
            "django.db.backends.sqlite3",
        )
