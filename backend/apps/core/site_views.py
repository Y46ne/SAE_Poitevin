from django.db.models import Q
from django.shortcuts import render
from django.utils import timezone

from apps.club.models import (
    AdministrativeDocument,
    ClubHistoryEntry,
    ClubProfile,
    ClubStaffMember,
)
from apps.competition.models import (
    Achievement,
    Competition,
    CompetitionEdition,
    Match,
    Team,
)
from apps.content.models import Article
from apps.open86.models import (
    OpenDraw,
    OpenEdition,
    OpenEditorial,
    OpenPhoto,
    OpenProgramItem,
)
from apps.partners.models import Partner, PartnerCategory
from apps.training.models import Coach, SportsSeason, TrainingOffer, TrainingPrice


def _public(queryset):
    field_names = {field.name for field in queryset.model._meta.get_fields()}
    if "is_published" in field_names:
        queryset = queryset.filter(is_published=True)
    if "published_at" in field_names:
        now = timezone.now()
        queryset = queryset.filter(
            Q(published_at__isnull=True) | Q(published_at__lte=now)
        )
    return queryset


def _label(item):
    for field in ("title", "name", "label", "competition_name"):
        value = getattr(item, field, "")
        if value:
            return str(value)
    first_name = getattr(item, "first_name", "")
    last_name = getattr(item, "last_name", "")
    if first_name or last_name:
        return f"{first_name} {last_name}".strip()
    return str(item)


def _group(title, queryset):
    return {"title": title, "items": [{"label": _label(item)} for item in queryset]}


def _section_groups():
    return {
        "club": (
        ("Présentation", ClubProfile.objects.all()),
        ("Histoire", _public(ClubHistoryEntry.objects.all())),
        ("Équipe", _public(ClubStaffMember.objects.all())),
        ("Documents administratifs", _public(AdministrativeDocument.objects.all())),
        ("Articles", _public(Article.objects.filter(scope=Article.SCOPE_CLUB))),
        ),
        "articles": (
        ("Articles du club", _public(Article.objects.filter(scope=Article.SCOPE_CLUB))),
        ("Articles de l'Open 86", _public(Article.objects.filter(scope=Article.SCOPE_OPEN))),
        ),
        "training": (
        ("Saisons", SportsSeason.objects.all()),
        ("Offres", _public(TrainingOffer.objects.all())),
        ("Tarifs", TrainingPrice.objects.select_related("offer", "season")),
        ("Enseignants", _public(Coach.objects.all())),
        ),
        "competition": (
        ("Compétitions", Competition.objects.all()),
        ("Éditions", CompetitionEdition.objects.all()),
        ("Équipes", Team.objects.all()),
        ("Matchs", Match.objects.all()),
        ("Palmarès", Achievement.objects.select_related("player")),
        ),
        "partners": (
        ("Catégories", PartnerCategory.objects.all()),
        ("Partenaires", Partner.objects.all()),
        ),
        "open86": (
        ("Éditions", _public(OpenEdition.objects.all())),
        ("Éditos", _public(OpenEditorial.objects.all())),
        ("Photos", _public(OpenPhoto.objects.all())),
        ("Programme du jour", _public(OpenProgramItem.objects.all())),
        ("Tableaux", _public(OpenDraw.objects.all())),
        ),
    }


def section_page(request, section):
    groups = [_group(title, queryset) for title, queryset in _section_groups()[section]]
    titles = {
        "club": "Le club",
        "articles": "Articles",
        "training": "Formation",
        "competition": "Compétition",
        "partners": "Partenaires",
        "open86": "Open Masculin 86",
    }
    return render(
        request,
        "section.html",
        {"section_title": titles[section], "groups": groups},
    )
