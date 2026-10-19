from django.db import models
from django.db.models import Q
from apps.core.models import MediaAsset, PublishableModel
from apps.competition.models import Player



from .open_draw import OpenDraw

class OpenDrawMatch(models.Model):
    draw = models.ForeignKey(OpenDraw, on_delete=models.CASCADE, related_name="matches")
    round_name = models.CharField(max_length=100)
    round_order = models.PositiveIntegerField(default=0)
    position = models.PositiveIntegerField(default=0)
    player_one_name = models.CharField(max_length=255, blank=True)
    player_two_name = models.CharField(max_length=255, blank=True)
    player_one = models.ForeignKey(Player, null=True, blank=True, on_delete=models.SET_NULL, related_name="open_draw_matches_one")
    player_two = models.ForeignKey(Player, null=True, blank=True, on_delete=models.SET_NULL, related_name="open_draw_matches_two")
    winner = models.ForeignKey(Player, null=True, blank=True, on_delete=models.SET_NULL, related_name="open_draw_wins")
    score_detail = models.JSONField(default=list, blank=True)
    scheduled_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["round_order", "position"]
        indexes = [models.Index(fields=["draw", "round_order", "position"])]

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.winner_id and self.winner_id not in {self.player_one_id, self.player_two_id}:
            raise ValidationError({"winner": "Le vainqueur doit être l'un des deux joueurs du match."})
        if self.player_one_id and self.player_two_id and self.player_one_id == self.player_two_id:
            raise ValidationError("Les deux joueurs d'un match doivent être différents.")
