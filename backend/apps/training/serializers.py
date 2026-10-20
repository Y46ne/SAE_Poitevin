from rest_framework import serializers

from apps.core.models import MediaAsset

from .models import Coach, SportsSeason, TrainingOffer, TrainingPrice


class TrainingMediaSerializer(serializers.ModelSerializer):
    url = serializers.FileField(source="file", read_only=True)

    class Meta:
        model = MediaAsset
        fields = ("id", "title", "alt_text", "url", "mime_type", "width", "height")


class SportsSeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsSeason
        fields = ("id", "label", "starts_on", "ends_on", "is_active")


class TrainingPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingPrice
        fields = ("id", "label", "amount", "currency", "unit", "description", "position", "season")


class TrainingOfferSerializer(serializers.ModelSerializer):
    prices = TrainingPriceSerializer(many=True, read_only=True)

    class Meta:
        model = TrainingOffer
        fields = ("id", "name", "slug", "description", "audience", "position", "prices")


class CoachSerializer(serializers.ModelSerializer):
    photo = TrainingMediaSerializer(read_only=True)
    offers = serializers.SlugRelatedField(many=True, read_only=True, slug_field="slug")

    class Meta:
        model = Coach
        fields = ("id", "first_name", "last_name", "qualification", "role", "biography", "photo", "private_lessons", "offers")
