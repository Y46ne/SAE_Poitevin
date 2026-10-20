from django.db.models import Prefetch, Q
from django.utils import timezone
from rest_framework import viewsets

from .models import (
    OpenDraw,
    OpenDrawMatch,
    OpenEdition,
    OpenEditorial,
    OpenPhoto,
    OpenProgramItem,
)
from .serializers import (
    OpenDrawMatchSerializer,
    OpenDrawSerializer,
    OpenEditionSerializer,
    OpenEditorialSerializer,
    OpenPhotoSerializer,
    OpenProgramItemSerializer,
)


class PublicOpenMixin:
    def public_editions(self):
        now = timezone.now()
        return OpenEdition.objects.filter(is_published=True).filter(
            Q(published_at__isnull=True) | Q(published_at__lte=now)
        )


class OpenEditionViewSet(PublicOpenMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = OpenEditionSerializer

    def get_queryset(self):
        return self.public_editions().select_related("logo", "banner")


class OpenEditorialViewSet(PublicOpenMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = OpenEditorialSerializer

    def get_queryset(self):
        now = timezone.now()
        return OpenEditorial.objects.filter(
            edition__in=self.public_editions(),
            is_published=True,
        ).filter(
            Q(published_at__isnull=True) | Q(published_at__lte=now)
        ).select_related("edition", "author_photo")


class OpenPhotoViewSet(PublicOpenMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = OpenPhotoSerializer

    def get_queryset(self):
        return OpenPhoto.objects.filter(edition__in=self.public_editions()).select_related(
            "edition", "image"
        )


class OpenProgramItemViewSet(PublicOpenMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = OpenProgramItemSerializer

    def get_queryset(self):
        return OpenProgramItem.objects.filter(
            edition__in=self.public_editions(), is_published=True
        ).select_related("edition")


class OpenDrawViewSet(PublicOpenMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = OpenDrawSerializer

    def get_queryset(self):
        matches = OpenDrawMatch.objects.select_related("player_one", "player_two", "winner")
        return OpenDraw.objects.filter(edition__in=self.public_editions()).select_related(
            "edition", "published_file"
        ).prefetch_related(Prefetch("matches", queryset=matches))


class OpenDrawMatchViewSet(PublicOpenMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = OpenDrawMatchSerializer

    def get_queryset(self):
        return OpenDrawMatch.objects.filter(
            draw__edition__in=self.public_editions()
        ).select_related("draw", "player_one", "player_two", "winner")
