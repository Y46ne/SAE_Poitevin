from rest_framework import serializers

from apps.core.models import MediaAsset

from ..models import Article


class ArticleMediaSerializer(serializers.ModelSerializer):
    url = serializers.FileField(source="file", read_only=True)

    class Meta:
        model = MediaAsset
        fields = ("id", "title", "alt_text", "url", "mime_type", "width", "height")


class ArticleListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    cover = ArticleMediaSerializer(read_only=True)

    class Meta:
        model = Article
        fields = (
            "id",
            "scope",
            "title",
            "slug",
            "excerpt",
            "cover",
            "category",
            "published_at",
        )


class ArticleDetailSerializer(ArticleListSerializer):
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field="slug")

    class Meta(ArticleListSerializer.Meta):
        fields = ArticleListSerializer.Meta.fields + ("body", "tags", "created_at", "updated_at")
