from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter

from albums.api.views import AlbumViewSet, TrackViewSet

router = SimpleRouter()
router.register(r'albums', AlbumViewSet, base_name='album')
router.register(r'tracks', TrackViewSet, base_name='track')

urlpatterns = [
    url(r'^', include(router.urls))
]

