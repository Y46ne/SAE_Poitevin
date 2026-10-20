from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from ..core.models import MediaAsset
from .models import Article, ArticleCategory, ArticleTag


class ArticleApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = ArticleCategory.objects.create(name="Vie du club", slug="vie-du-club")
        self.tag = ArticleTag.objects.create(name="Actualité", slug="actualite")
        self.published_article = Article.objects.create(
            scope=Article.SCOPE_CLUB,
            title="Article publié",
            slug="article-publie",
            body="Contenu",
            category=self.category,
            is_published=True,
        )
        self.published_article.tags.add(self.tag)
        Article.objects.create(
            scope=Article.SCOPE_CLUB,
            title="Article brouillon",
            slug="article-brouillon",
            body="Contenu",
        )

    def test_list_returns_only_published_articles(self):
        response = self.client.get("/api/v1/articles/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["slug"], "article-publie")

    def test_detail_uses_slug_and_returns_tags(self):
        response = self.client.get("/api/v1/articles/article-publie/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["tags"], ["actualite"])
        self.assertEqual(response.data["body"], "Contenu")

    def test_filters_by_category_and_tag(self):
        category_response = self.client.get("/api/v1/articles/?category=vie-du-club")
        tag_response = self.client.get("/api/v1/articles/?tag=actualite")

        self.assertEqual(category_response.data["count"], 1)
        self.assertEqual(tag_response.data["count"], 1)
