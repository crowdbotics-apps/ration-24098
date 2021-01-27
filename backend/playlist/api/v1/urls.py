from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import PlaylistViewSet

router = DefaultRouter()
router.register("playlist", PlaylistViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
