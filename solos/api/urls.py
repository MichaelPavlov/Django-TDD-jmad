from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter

from solos.api.views import SoloViewSet

router = SimpleRouter()
router.register(r'solos', SoloViewSet, base_name='solo')

urlpatterns = [
    url(r'^', include(router.urls))
]
