from rest_framework import serializers

from apps.core.models import MediaAsset

from .models import (
    AdministrativeDocument,
    ClubHistoryEntry,
    ClubProfile,
    ClubStaffMember,
)


class ClubMediaSerializer(serializers.ModelSerializer):
    url = serializers.FileField(source="file", read_only=True)

    class Meta:
        model = MediaAsset
        fields = ("id", "title", "alt_text", "url", "mime_type", "width", "height")


class ClubProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubProfile
        fields = (
            "id",
            "name",
            "short_description",
            "description",
            "address",
            "email",
            "phone",
            "website",
        )


class ClubHistoryEntrySerializer(serializers.ModelSerializer):
    image = ClubMediaSerializer(read_only=True)

    class Meta:
        model = ClubHistoryEntry
        fields = (
            "id",
            "year",
            "title",
            "description",
            "image",
            "position",
        )


class ClubStaffMemberSerializer(serializers.ModelSerializer):
    photo = ClubMediaSerializer(read_only=True)

    class Meta:
        model = ClubStaffMember
        fields = (
            "id",
            "first_name",
            "last_name",
            "role",
            "biography",
            "photo",
            "email",
            "phone",
            "position",
        )


class AdministrativeDocumentSerializer(serializers.ModelSerializer):
    url = serializers.FileField(source="file", read_only=True)

    class Meta:
        model = AdministrativeDocument
        fields = (
            "id",
            "title",
            "category",
            "url",
            "description",
            "published_at",
        )
