from rest_framework.routers import DefaultRouter

from .views import CoachViewSet, SportsSeasonViewSet, TrainingOfferViewSet, TrainingPriceViewSet

router = DefaultRouter()
router.register("seasons", SportsSeasonViewSet, basename="training-season")
router.register("offers", TrainingOfferViewSet, basename="training-offer")
router.register("prices", TrainingPriceViewSet, basename="training-price")
router.register("coaches", CoachViewSet, basename="coach")

urlpatterns = router.urls
