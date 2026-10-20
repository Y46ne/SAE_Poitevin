from rest_framework.routers import DefaultRouter

from .views import (
    AchievementViewSet,
    CompetitionEditionViewSet,
    CompetitionTeamViewSet,
    CompetitionViewSet,
    MatchViewSet,
    PlayerViewSet,
    TeamPlayerViewSet,
    TeamViewSet,
)

router = DefaultRouter()
router.register("competitions", CompetitionViewSet, basename="competition")
router.register("editions", CompetitionEditionViewSet, basename="competition-edition")
router.register("teams", TeamViewSet, basename="team")
router.register("competition-teams", CompetitionTeamViewSet, basename="competition-team")
router.register("matches", MatchViewSet, basename="match")
router.register("players", PlayerViewSet, basename="player")
router.register("team-players", TeamPlayerViewSet, basename="team-player")
router.register("achievements", AchievementViewSet, basename="achievement")

urlpatterns = router.urls
