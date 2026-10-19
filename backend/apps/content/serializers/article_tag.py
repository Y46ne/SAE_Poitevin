from rest_framework import serializers

from ..models import ArticleTag


class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = ("id", "name", "slug")
