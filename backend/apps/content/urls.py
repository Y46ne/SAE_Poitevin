from rest_framework.routers import DefaultRouter

from .views import ArticleCategoryViewSet, ArticleTagViewSet, ArticleViewSet

router = DefaultRouter()
router.register("articles", ArticleViewSet, basename="article")
router.register("categories", ArticleCategoryViewSet, basename="article-category")
router.register("tags", ArticleTagViewSet, basename="article-tag")

urlpatterns = router.urls
