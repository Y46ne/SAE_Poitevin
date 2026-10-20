from rest_framework import viewsets

from .models import (
    Achievement,
    Competition,
    CompetitionEdition,
    CompetitionTeam,
    Match,
    Player,
    Team,
    TeamPlayer,
)
from .serializers import (
    AchievementSerializer,
    CompetitionEditionSerializer,
    CompetitionSerializer,
    CompetitionTeamSerializer,
    MatchSerializer,
    PlayerSerializer,
    TeamPlayerSerializer,
    TeamSerializer,
)


class CompetitionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    lookup_field = "slug"


class CompetitionEditionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CompetitionEdition.objects.select_related("competition", "season").filter(is_active=True)
    serializer_class = CompetitionEditionSerializer


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class CompetitionTeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CompetitionTeam.objects.select_related(
        "edition__competition", "edition__season", "team"
    )
    serializer_class = CompetitionTeamSerializer


class MatchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Match.objects.select_related(
        "edition__competition", "edition__season", "home_team", "away_team"
    )
    serializer_class = MatchSerializer


class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class TeamPlayerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TeamPlayer.objects.select_related("team", "player", "season")
    serializer_class = TeamPlayerSerializer


class AchievementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Achievement.objects.select_related("player")
    serializer_class = AchievementSerializer
