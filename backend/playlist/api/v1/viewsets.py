from rest_framework import authentication
from playlist.models import Playlist
from .serializers import PlaylistSerializer
from rest_framework import viewsets


class PlaylistViewSet(viewsets.ModelViewSet):
    serializer_class = PlaylistSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Playlist.objects.all()
