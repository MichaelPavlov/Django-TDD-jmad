from rest_framework.serializers import HyperlinkedModelSerializer

from albums.models import Album


class AlbumSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
        extra_kwargs= {
            'url': {'view_name': 'api:album-detail'}
        }
