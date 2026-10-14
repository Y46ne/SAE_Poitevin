"""Database models for the legacy content application."""

from .user import User
from .categorie import Categorie
from .tag import Tag
from .page import Page
from .competition import Competition
from .equipe import Equipe
from .match_tennis import MatchTennis
from .joueur import Joueur
from .palmares import Palmares
from .couleur_site import CouleurSite
from .cours_formation import CoursFormation
from .tarif_formation import TarifFormation
from .domaine import Domaine
from .partenaire import Partenaire
from .enseignant import Enseignant
from .membre_management import MembreManagement
from .document_administratif import DocumentAdministratif
from .histoire_club import HistoireClub
from .media import Media
from .section_accueil import SectionAccueil
from .navbar import Navbar
from .navbar_item import NavbarItem
from .footer import Footer
from .footer_row import FooterRow
from .footer_column import FooterColumn
from .footer_item import FooterItem
from .open86_config import Open86Config
from .open86_couleur_site import Open86CouleurSite
from .open86_domaine import Open86Domaine
from .open86_partenaire import Open86Partenaire
from .open86_edito import Open86Edito
from .open86_section_accueil import Open86SectionAccueil
from .open86_navbar import Open86Navbar
from .open86_navbar_item import Open86NavbarItem
from .open86_footer import Open86Footer
from .open86_footer_row import Open86FooterRow
from .open86_footer_column import Open86FooterColumn
from .open86_footer_item import Open86FooterItem

__all__ = [
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
]
