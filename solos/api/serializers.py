from rest_framework.serializers import HyperlinkedModelSerializer

from albums.models import Album, Track


class AlbumSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'api:album-detail'}
        }


class TrackSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'api:track-detail'},
            'album': {'view_name': 'api:album-detail'},
        }
