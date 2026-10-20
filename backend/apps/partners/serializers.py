from rest_framework import serializers

from apps.core.models import MediaAsset

from .models import Partner, PartnerCategory, PartnerPlacement


class PartnerMediaSerializer(serializers.ModelSerializer):
    url = serializers.FileField(source="file", read_only=True)

    class Meta:
        model = MediaAsset
        fields = ("id", "title", "alt_text", "url", "mime_type", "width", "height")


class PartnerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerCategory
        fields = ("id", "name", "position")


class PartnerSerializer(serializers.ModelSerializer):
    logo = PartnerMediaSerializer(read_only=True)
    category = PartnerCategorySerializer(read_only=True)

    class Meta:
        model = Partner
        fields = ("id", "name", "slug", "logo", "website", "description", "category", "is_active")


class PartnerPlacementSerializer(serializers.ModelSerializer):
    partner = PartnerSerializer(read_only=True)

    class Meta:
        model = PartnerPlacement
        fields = ("id", "partner", "sponsorship_level", "position", "club", "open_edition")
