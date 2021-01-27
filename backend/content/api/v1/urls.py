from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ContentViewSet

router = DefaultRouter()
router.register("content", ContentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
