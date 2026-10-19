from django.db import models
from django.db.models import Q
from apps.core.models import MediaAsset


class PartnerCategory(models.Model):
    name = models.CharField(max_length=100)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position", "name"]
        indexes = [models.Index(fields=["position"])]


class Partner(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    logo = models.ForeignKey(MediaAsset, null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(PartnerCategory, null=True, blank=True, on_delete=models.SET_NULL, related_name="partners")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["is_active"]), models.Index(fields=["category", "is_active"])]


class PartnerPlacement(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.PROTECT, related_name="placements")
    club = models.ForeignKey("club.ClubProfile", null=True, blank=True, on_delete=models.CASCADE, related_name="partner_placements")
    open_edition = models.ForeignKey("open86.OpenEdition", null=True, blank=True, on_delete=models.CASCADE, related_name="partner_placements")
    sponsorship_level = models.CharField(max_length=100, blank=True)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position", "partner__name"]
        indexes = [models.Index(fields=["partner", "position"]), models.Index(fields=["club", "position"]), models.Index(fields=["open_edition", "position"])]
        constraints = [models.CheckConstraint(condition=Q(club__isnull=False, open_edition__isnull=True) | Q(club__isnull=True, open_edition__isnull=False), name="partner_placement_has_one_scope")]

    def clean(self):
        from django.core.exceptions import ValidationError

        if (self.club_id is None) == (self.open_edition_id is None):
            raise ValidationError(
                "Un partenaire doit être rattaché au club ou à une édition Open, mais pas aux deux."
            )
