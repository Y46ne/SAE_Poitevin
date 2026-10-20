from rest_framework import viewsets

from .models import Partner, PartnerCategory, PartnerPlacement
from .serializers import PartnerCategorySerializer, PartnerPlacementSerializer, PartnerSerializer


class PartnerCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PartnerCategory.objects.all()
    serializer_class = PartnerCategorySerializer


class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PartnerSerializer

    def get_queryset(self):
        return Partner.objects.filter(is_active=True).select_related("logo", "category")


class PartnerPlacementViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PartnerPlacementSerializer

    def get_queryset(self):
        return PartnerPlacement.objects.filter(partner__is_active=True).select_related(
            "partner__logo", "partner__category", "club", "open_edition"
        )
