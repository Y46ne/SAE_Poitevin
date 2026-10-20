from django.db.models import Q
from django.utils import timezone
from rest_framework import viewsets

from .models import (
    AdministrativeDocument,
    ClubHistoryEntry,
    ClubProfile,
    ClubStaffMember,
)
from .serializers import (
    AdministrativeDocumentSerializer,
    ClubHistoryEntrySerializer,
    ClubProfileSerializer,
    ClubStaffMemberSerializer,
)


class PublicClubQuerysetMixin:
    def public_queryset(self, queryset):
        now = timezone.now()
        return queryset.filter(is_published=True).filter(
            Q(published_at__isnull=True) | Q(published_at__lte=now)
        )


class ClubProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClubProfile.objects.all()
    serializer_class = ClubProfileSerializer


class ClubHistoryEntryViewSet(PublicClubQuerysetMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = ClubHistoryEntrySerializer

    def get_queryset(self):
        return self.public_queryset(
            ClubHistoryEntry.objects.select_related("image")
        )


class ClubStaffMemberViewSet(PublicClubQuerysetMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = ClubStaffMemberSerializer

    def get_queryset(self):
        return self.public_queryset(
            ClubStaffMember.objects.select_related("photo")
        )


class AdministrativeDocumentViewSet(
    PublicClubQuerysetMixin, viewsets.ReadOnlyModelViewSet
):
    serializer_class = AdministrativeDocumentSerializer

    def get_queryset(self):
        return self.public_queryset(AdministrativeDocument.objects.all())
