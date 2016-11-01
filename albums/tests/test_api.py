from urllib.parse import urljoin

from django.core.urlresolvers import resolve
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from albums.models import Album, Track

HOST = 'http://testserver'


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

        album_url = reverse('api:album-detail', kwargs={"pk": self.kind_of_blue.id})
        album_url = urljoin(HOST, album_url)
        response = self.client.get(albums_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'A Love Supreme')
        self.assertEqual(response.data[1]['url'], album_url)

    def test_album_list_route(self):
        """
        Test that we've got routing set up for Albums
        """
        albums_url = reverse('api:album-list')
        route = resolve(albums_url)
        self.assertEqual(route.func.__name__, 'AlbumViewSet')


class TrackAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.no_funny_hats = Album.objects.create(
            name='No Funny Hats',
            slug='no-funny-hats',
        )

        cls.bugle_call_rag = Track.objects.create(
            name='Bugle Call Rag',
            album=cls.no_funny_hats,
            slug='bugle-call-rag',
        )

        cls.giant_steps = Album.objects.create(
            name='Giant Steps',
            slug='giant-steps',
        )

        cls.mr_pc = Track.objects.create(
            name='Mr. PC',
            slug='mr-pc',
            album=cls.giant_steps,
        )

    def test_list_tracks(self):
        """
        Test that we can get a list of tracks
        """
        tracks_url = reverse('api:track-list')
        track_url = reverse('api:track-detail', kwargs={"pk": self.bugle_call_rag.id})
        track_url = urljoin(HOST, track_url)
        response = self.client.get(tracks_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], self.mr_pc.name)
        self.assertEqual(response.data[1]['url'], track_url)

    def test_track_list_route(self):
        """
        Test that we've got routing set up for Tracks
        """
        tracks_url = reverse('api:track-list')
        route = resolve(tracks_url)
        self.assertEqual(route.func.__name__, 'TrackViewSet')
