from rest_framework.routers import DefaultRouter

from .views import (
    AdministrativeDocumentViewSet,
    ClubHistoryEntryViewSet,
    ClubProfileViewSet,
    ClubStaffMemberViewSet,
)

router = DefaultRouter()
router.register("profile", ClubProfileViewSet, basename="club-profile")
router.register("history", ClubHistoryEntryViewSet, basename="club-history")
router.register("management", ClubStaffMemberViewSet, basename="club-management")
router.register("documents", AdministrativeDocumentViewSet, basename="club-document")

urlpatterns = router.urls
