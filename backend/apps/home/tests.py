from django.test import TestCase
from django.urls import reverse

from .models import HomeBlock, HomePage


class HomePageViewTests(TestCase):
    def test_home_page_renders_published_blocks(self):
        page = HomePage.objects.create(name="Accueil du club")
        HomeBlock.objects.create(
            home_page=page,
            block_type=HomeBlock.TYPE_INFO,
            title="Actualités",
            is_published=True,
        )
        HomeBlock.objects.create(
            home_page=page,
            block_type=HomeBlock.TYPE_INFO,
            title="Brouillon",
            is_published=False,
            position=1,
        )

        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["home_data"]["blocks"][0]["title"], "Actualités")
        self.assertNotIn(
            "Brouillon",
            [block["title"] for block in response.context["home_data"]["blocks"]],
        )

    def test_home_page_returns_not_found_without_active_page(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 404)
