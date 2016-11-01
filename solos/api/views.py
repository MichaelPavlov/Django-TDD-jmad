from rest_framework.viewsets import ModelViewSet

from solos.api.serializers import SoloSerializer
from solos.models import Solo


class SoloViewSet(ModelViewSet):
    queryset = Solo.objects.all()
    serializer_class = SoloSerializer
