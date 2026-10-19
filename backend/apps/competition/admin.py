from django.contrib import admin
from .models import Achievement, Competition, CompetitionEdition, CompetitionTeam, Match, Player, Team, TeamPlayer

admin.site.register((Achievement, Competition, CompetitionEdition, CompetitionTeam, Match, Player, Team, TeamPlayer))
