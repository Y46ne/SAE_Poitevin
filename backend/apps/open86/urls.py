from rest_framework.routers import DefaultRouter

from .views import (
    OpenDrawMatchViewSet,
    OpenDrawViewSet,
    OpenEditionViewSet,
    OpenEditorialViewSet,
    OpenPhotoViewSet,
    OpenProgramItemViewSet,
)

router = DefaultRouter()
router.register("editions", OpenEditionViewSet, basename="open-edition")
router.register("editorials", OpenEditorialViewSet, basename="open-editorial")
router.register("photos", OpenPhotoViewSet, basename="open-photo")
router.register("program", OpenProgramItemViewSet, basename="open-program")
router.register("draws", OpenDrawViewSet, basename="open-draw")
router.register("draw-matches", OpenDrawMatchViewSet, basename="open-draw-match")

urlpatterns = router.urls
