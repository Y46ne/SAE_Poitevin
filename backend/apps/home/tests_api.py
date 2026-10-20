from datetime import timedelta

from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIClient

from apps.competition.models import Competition
from apps.content.models import Article
from apps.partners.models import Partner

from .models import HomeBlock, HomePage


class HomeApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.home_page = HomePage.objects.create(name="Accueil principale")
        self.article = Article.objects.create(
            scope=Article.SCOPE_CLUB,
            title="Article accueil",
            slug="article-accueil",
            body="Contenu",
            is_published=True,
        )
        self.competition = Competition.objects.create(
            name="Championnat régional",
            slug="championnat-regional",
            competition_type="championship",
        )
        self.partner = Partner.objects.create(
            name="Partenaire accueil",
            slug="partenaire-accueil",
        )
        self.block = HomeBlock.objects.create(
            home_page=self.home_page,
            block_type=HomeBlock.TYPE_INFO,
            title="À la une",
            is_published=True,
        )
        self.block.articles.add(self.article)
        self.block.competitions.add(self.competition)
        self.block.partners.add(self.partner)

    def test_returns_active_home_page_with_related_content(self):
        response = self.client.get("/api/v1/home/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Accueil principale")
        self.assertEqual(len(response.data["blocks"]), 1)
        block = response.data["blocks"][0]
        self.assertEqual(block["articles"][0]["slug"], "article-accueil")
        self.assertEqual(block["competitions"][0]["slug"], "championnat-regional")
        self.assertEqual(block["partners"][0]["slug"], "partenaire-accueil")

    def test_hides_unpublished_and_expired_blocks(self):
        HomeBlock.objects.create(
            home_page=self.home_page,
            block_type=HomeBlock.TYPE_INFO,
            title="Brouillon",
            position=1,
        )
        HomeBlock.objects.create(
            home_page=self.home_page,
            block_type=HomeBlock.TYPE_INFO,
            title="Expiré",
            is_published=True,
            ends_at=timezone.now() - timedelta(days=1),
            position=2,
        )

        response = self.client.get("/api/v1/home/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual([block["title"] for block in response.data["blocks"]], ["À la une"])

    def test_hides_unpublished_articles_in_blocks(self):
        draft = Article.objects.create(
            scope=Article.SCOPE_CLUB,
            title="Article brouillon",
            slug="article-brouillon",
            body="Contenu",
        )
        self.block.articles.add(draft)

        response = self.client.get("/api/v1/home/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            [article["slug"] for article in response.data["blocks"][0]["articles"]],
            ["article-accueil"],
        )

    def test_returns_not_found_without_active_home_page(self):
        HomePage.objects.all().delete()

        response = self.client.get("/api/v1/home/")

        self.assertEqual(response.status_code, 404)
