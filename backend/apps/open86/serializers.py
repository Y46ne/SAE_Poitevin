from rest_framework import serializers

from apps.core.models import MediaAsset
from apps.competition.models import Player

from .models import (
    OpenDraw,
    OpenDrawMatch,
    OpenEdition,
    OpenEditorial,
    OpenPhoto,
    OpenProgramItem,
)


class OpenMediaSerializer(serializers.ModelSerializer):
    url = serializers.FileField(source="file", read_only=True)

    class Meta:
        model = MediaAsset
        fields = ("id", "title", "alt_text", "url", "mime_type", "width", "height")


class OpenEditionSerializer(serializers.ModelSerializer):
    logo = OpenMediaSerializer(read_only=True)
    banner = OpenMediaSerializer(read_only=True)

    class Meta:
        model = OpenEdition
        fields = (
            "id", "year", "title", "subtitle", "description", "logo", "banner",
            "starts_at", "ends_at", "is_current", "is_archived",
        )


class OpenEditorialSerializer(serializers.ModelSerializer):
    author_photo = OpenMediaSerializer(read_only=True)

    class Meta:
        model = OpenEditorial
        fields = (
            "id", "edition", "title", "author_name", "author_role", "author_photo",
            "body", "position", "published_at",
        )


class OpenPhotoSerializer(serializers.ModelSerializer):
    image = OpenMediaSerializer(read_only=True)

    class Meta:
        model = OpenPhoto
        fields = ("id", "edition", "image", "caption", "alt_text", "position")


class OpenProgramItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenProgramItem
        fields = (
            "id", "edition", "title", "description", "starts_at", "ends_at",
            "location", "category", "position",
        )


class OpenDrawMatchSerializer(serializers.ModelSerializer):
    player_one = serializers.PrimaryKeyRelatedField(read_only=True)
    player_two = serializers.PrimaryKeyRelatedField(read_only=True)
    winner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = OpenDrawMatch
        fields = (
            "id", "draw", "round_name", "round_order", "position",
            "player_one_name", "player_two_name", "player_one", "player_two",
            "winner", "score_detail", "scheduled_at",
        )


class OpenDrawSerializer(serializers.ModelSerializer):
    published_file = OpenMediaSerializer(read_only=True)
    matches = OpenDrawMatchSerializer(many=True, read_only=True)

    class Meta:
        model = OpenDraw
        fields = ("id", "edition", "name", "category", "draw_type", "published_file", "position", "matches")
