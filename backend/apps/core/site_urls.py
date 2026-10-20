from django.urls import path

from .site_views import section_page

urlpatterns = [
    path("club/", section_page, {"section": "club"}, name="club"),
    path("articles/", section_page, {"section": "articles"}, name="articles"),
    path("training/", section_page, {"section": "training"}, name="training"),
    path("competition/", section_page, {"section": "competition"}, name="competition"),
    path("partners/", section_page, {"section": "partners"}, name="partners"),
    path("open86/", section_page, {"section": "open86"}, name="open86"),
]
