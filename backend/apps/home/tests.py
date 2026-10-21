from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from apps.club.models import ClubProfile

from .models import HomeBlock, HomePage


class HomePageViewTests(TestCase):
    def setUp(self):
        self.page = HomePage.objects.create(name="Accueil du club")

    def add_block(self, title, position, **fields):
        return HomeBlock.objects.create(
            home_page=self.page,
            block_type=HomeBlock.TYPE_INFO,
            title=title,
            position=position,
            **fields,
        )

    def test_home_page_renders_published_blocks_in_html(self):
        self.add_block("Actualités", 0, is_published=True, subtitle="Rentrée du club")
        self.add_block("Brouillon", 1, is_published=False)

        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Navigation principale")
        self.assertContains(response, 'href="/club/"')
        self.assertContains(response, "<h1>Stade Poitevin Tennis</h1>", html=True)
        self.assertContains(response, "Actualités")
        self.assertContains(response, "Rentrée du club")
        self.assertContains(response, "Information")
        self.assertNotContains(response, "Brouillon")

    def test_home_page_hides_blocks_outside_display_dates(self):
        now = timezone.now()
        self.add_block("En cours", 0, is_published=True, starts_at=now - timedelta(days=1))
        self.add_block("Terminé", 1, is_published=True, ends_at=now - timedelta(days=1))
        self.add_block("À venir", 2, is_published=True, starts_at=now + timedelta(days=1))
        self.add_block("Pas encore publié", 3, is_published=True, published_at=now + timedelta(days=1))

        response = self.client.get(reverse("home"))

        self.assertContains(response, "En cours")
        self.assertNotContains(response, "Terminé")
        self.assertNotContains(response, "À venir")
        self.assertNotContains(response, "Pas encore publié")

    def test_home_page_shows_info_blocks_with_value_as_figures(self):
        self.add_block("Courts", 0, is_published=True, settings={"value": "9"})
        self.add_block("Rentrée", 1, is_published=True)

        response = self.client.get(reverse("home"))

        self.assertContains(response, '<p class="figure-value">9</p>', html=True)
        self.assertEqual([block.title for block in response.context["figures"]], ["Courts"])
        self.assertEqual([block.title for block in response.context["featured"]], ["Rentrée"])

    def test_home_page_uses_club_profile_for_hero(self):
        ClubProfile.objects.create(name="Stade Poitevin TC", short_description="Tennis et padel.")

        response = self.client.get(reverse("home"))

        self.assertContains(response, "<h1>Stade Poitevin TC</h1>", html=True)
        self.assertContains(response, '<meta property="og:description" content="Tennis et padel.">', html=True)

    def test_home_page_shows_empty_state_without_blocks(self):
        response = self.client.get(reverse("home"))

        self.assertContains(response, "Les actualités du club arrivent bientôt.")

    def test_home_page_does_not_load_vue(self):
        response = self.client.get(reverse("home"))

        self.assertContains(response, "frontend/app.css")
        self.assertNotContains(response, "frontend/app.js")

    def test_home_page_returns_not_found_without_active_page(self):
        self.page.is_active = False
        self.page.save()

        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 404)
