from django.test import SimpleTestCase

from legacy import models


def _module_name(class_name):
    return "".join(
        f"_{character.lower()}" if character.isupper() and index else character
        for index, character in enumerate(class_name)
    ).lstrip("_")


class ModelModuleStructureTests(SimpleTestCase):
    """Ensure every legacy model remains available from its own module."""

    MODEL_NAMES = (
        "User",
        "Categorie",
        "Tag",
        "Page",
        "Competition",
        "Equipe",
        "MatchTennis",
        "Joueur",
        "Palmares",
        "CouleurSite",
        "CoursFormation",
        "TarifFormation",
        "Domaine",
        "Partenaire",
        "Enseignant",
        "MembreManagement",
        "DocumentAdministratif",
        "HistoireClub",
        "Media",
        "SectionAccueil",
        "Navbar",
        "NavbarItem",
        "Footer",
        "FooterRow",
        "FooterColumn",
        "FooterItem",
        "Open86Config",
        "Open86CouleurSite",
        "Open86Domaine",
        "Open86Partenaire",
        "Open86Edito",
        "Open86SectionAccueil",
        "Open86Navbar",
        "Open86NavbarItem",
        "Open86Footer",
        "Open86FooterRow",
        "Open86FooterColumn",
        "Open86FooterItem",
    )

    def test_models_are_reexported_and_defined_in_dedicated_modules(self):
        for model_name in self.MODEL_NAMES:
            model = getattr(models, model_name)
            self.assertEqual(model.__module__, f"legacy.models.{_module_name(model_name)}")