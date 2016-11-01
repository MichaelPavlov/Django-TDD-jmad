from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter

from albums.api.views import AlbumViewSet

router = SimpleRouter()
router.register(r'albums', AlbumViewSet, base_name='album')

urlpatterns = [
    url(r'^', include(router.urls))
]

