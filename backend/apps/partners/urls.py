from rest_framework.routers import DefaultRouter

from .views import PartnerCategoryViewSet, PartnerPlacementViewSet, PartnerViewSet

router = DefaultRouter()
router.register("categories", PartnerCategoryViewSet, basename="partner-category")
router.register("partners", PartnerViewSet, basename="partner")
router.register("placements", PartnerPlacementViewSet, basename="partner-placement")

urlpatterns = router.urls
