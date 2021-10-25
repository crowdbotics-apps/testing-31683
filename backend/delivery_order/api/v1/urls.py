from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import OrderViewSet, BillViewSet, PaymentMethodViewSet

router = DefaultRouter()
router.register("order", OrderViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("bill", BillViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
