from rest_framework import serializers

from apps.competition.models import Competition
from apps.content.models import Article
from apps.partners.models import Partner

from .models import HomeBlock, HomePage


class HomeArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "scope", "title", "slug", "excerpt", "published_at")


class HomeCompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ("id", "name", "slug", "competition_type", "description")


class HomePartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ("id", "name", "slug", "website", "description")


class HomeBlockSerializer(serializers.ModelSerializer):
    articles = HomeArticleSerializer(many=True, read_only=True)
    competitions = HomeCompetitionSerializer(many=True, read_only=True)
    partners = HomePartnerSerializer(many=True, read_only=True)

    class Meta:
        model = HomeBlock
        fields = (
            "id",
            "block_type",
            "title",
            "subtitle",
            "position",
            "starts_at",
            "ends_at",
            "settings",
            "articles",
            "competitions",
            "partners",
        )


class HomePageSerializer(serializers.ModelSerializer):
    blocks = HomeBlockSerializer(many=True, read_only=True)

    class Meta:
        model = HomePage
        fields = ("id", "name", "blocks")
