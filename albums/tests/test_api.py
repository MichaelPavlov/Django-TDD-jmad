from urllib.parse import urljoin

from django.core.urlresolvers import resolve
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from albums.models import Album


class AlbumAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.kind_of_blue = Album.objects.create(name='Kind of Blue')
        cls.a_love_supreme = Album.objects.create(name='A Love Supreme')

    def test_list_albums(self):
        """
        Test that we can get a list of albums
        """
        albums_url = reverse('api:album-list')
        host = 'http://testserver'
        album_url = reverse('api:album-detail', kwargs={"pk": self.kind_of_blue.id})
        album_url = urljoin(host, album_url)
        response = self.client.get(albums_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'A Love Supreme')
        self.assertEqual(response.data[1]['url'], album_url)

    def test_album_list_route(self):
        """
        Test that we've got routing set up for Albums
        """
        albums_url = reverse('api:album-list')
        route = resolve(albums_url)
        self.assertEqual(route.func.__name__, 'AlbumViewSet')
