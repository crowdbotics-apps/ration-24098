from rest_framework import authentication
from content.models import Content
from .serializers import ContentSerializer
from rest_framework import viewsets


class ContentViewSet(viewsets.ModelViewSet):
    serializer_class = ContentSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Content.objects.all()
