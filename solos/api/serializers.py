from rest_framework.serializers import HyperlinkedModelSerializer

from solos.models import Solo


class SoloSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Solo
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'api:solo-detail'}
        }
