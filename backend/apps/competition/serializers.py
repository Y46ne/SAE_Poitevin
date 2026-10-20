from rest_framework import serializers

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


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ("id", "name", "slug", "competition_type", "description")


class CompetitionEditionSerializer(serializers.ModelSerializer):
    competition = CompetitionSerializer(read_only=True)

    class Meta:
        model = CompetitionEdition
        fields = (
            "id", "competition", "season", "category", "division", "group",
            "gender", "starts_on", "ends_on", "final_ranking", "is_active",
        )


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ("id", "name", "city", "is_club_team")


class CompetitionTeamSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    edition = CompetitionEditionSerializer(read_only=True)

    class Meta:
        model = CompetitionTeam
        fields = ("id", "edition", "team")


class MatchSerializer(serializers.ModelSerializer):
    edition = CompetitionEditionSerializer(read_only=True)
    home_team = TeamSerializer(read_only=True)
    away_team = TeamSerializer(read_only=True)

    class Meta:
        model = Match
        fields = (
            "id", "edition", "home_team", "away_team", "scheduled_at", "venue",
            "home_score", "away_score", "score_detail", "status", "is_forfeit", "comment",
        )


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ("id", "first_name", "last_name", "gender", "category", "current_ranking")


class TeamPlayerSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    player = PlayerSerializer(read_only=True)

    class Meta:
        model = TeamPlayer
        fields = ("id", "team", "player", "season")


class AchievementSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)

    class Meta:
        model = Achievement
        fields = ("id", "player", "year", "competition_name", "result", "category", "level", "event")
