from rest_framework.viewsets import ModelViewSet

from albums.models import Album, Track
from solos.api.serializers import AlbumSerializer, TrackSerializer


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class TrackViewSet(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
