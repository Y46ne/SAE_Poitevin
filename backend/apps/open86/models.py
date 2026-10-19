from django.db import models
from django.db.models import Q
from apps.core.models import MediaAsset, PublishableModel
from apps.competition.models import Player


class OpenEdition(PublishableModel):
    year = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=255, default="Open Masculin 86")
    subtitle = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    logo = models.ForeignKey(MediaAsset, null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    banner = models.ForeignKey(MediaAsset, null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    starts_at = models.DateTimeField(null=True, blank=True)
    ends_at = models.DateTimeField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)

    class Meta:
        ordering = ["-year"]
        indexes = [models.Index(fields=["is_published", "-year"]), models.Index(fields=["is_current"])]
        constraints = [
            models.UniqueConstraint(fields=["is_current"], condition=Q(is_current=True), name="one_current_open_edition"),
            models.CheckConstraint(condition=Q(ends_at__isnull=True) | Q(starts_at__isnull=True) | Q(ends_at__gte=models.F("starts_at")), name="open_edition_ends_after_start"),
        ]


class OpenEditorial(PublishableModel):
    edition = models.ForeignKey(OpenEdition, on_delete=models.CASCADE, related_name="editorials")
    title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    author_role = models.CharField(max_length=255, blank=True)
    author_photo = models.ForeignKey(MediaAsset, null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    body = models.TextField()
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position", "id"]
        indexes = [models.Index(fields=["edition", "position"]), models.Index(fields=["is_published"])]


class OpenPhoto(models.Model):
    edition = models.ForeignKey(OpenEdition, on_delete=models.CASCADE, related_name="photos")
    image = models.ForeignKey(MediaAsset, on_delete=models.PROTECT, related_name="+")
    caption = models.CharField(max_length=255, blank=True)
    alt_text = models.CharField(max_length=255)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position", "id"]
        indexes = [models.Index(fields=["edition", "position"])]


class OpenProgramItem(models.Model):
    edition = models.ForeignKey(OpenEdition, on_delete=models.CASCADE, related_name="program_items")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=100, blank=True)
    is_published = models.BooleanField(default=True)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["starts_at", "position"]
        indexes = [models.Index(fields=["edition", "starts_at", "is_published"])]
        constraints = [models.CheckConstraint(condition=Q(ends_at__isnull=True) | Q(ends_at__gte=models.F("starts_at")), name="open_program_ends_after_start")]


class OpenDraw(models.Model):
    DRAW_CHOICES = (("main", "Tableau final"), ("qualifying", "Qualifications"))
    edition = models.ForeignKey(OpenEdition, on_delete=models.CASCADE, related_name="draws")
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100, blank=True)
    draw_type = models.CharField(max_length=20, choices=DRAW_CHOICES)
    published_file = models.ForeignKey(MediaAsset, null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position", "name"]
        indexes = [models.Index(fields=["edition", "draw_type"])]


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
