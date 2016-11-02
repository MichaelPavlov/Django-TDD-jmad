from django.utils.text import slugify
from rest_framework.serializers import HyperlinkedModelSerializer

from solos.models import Solo


class SoloSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Solo
        fields = '__all__'
        read_only_fields = ['slug']
        extra_kwargs = {
            'url': {'view_name': 'api:solo-detail'},
            'track': {'view_name': 'api:track-detail'},
        }

    def validate(self, data):
        data['slug'] = slugify(data['artist'])
        return data
