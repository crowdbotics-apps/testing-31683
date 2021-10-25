from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    ReviewViewSet,
    ItemViewSet,
    CategoryViewSet,
    CountryViewSet,
    ItemVariantViewSet,
)

router = DefaultRouter()
router.register("review", ReviewViewSet)
router.register("country", CountryViewSet)
router.register("item", ItemViewSet)
router.register("itemvariant", ItemVariantViewSet)
router.register("category", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
