from django.core.urlresolvers import resolve
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from albums.models import Album, Track


class SoloAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.giant_steps = Album.objects.create(name='Giant Steps', slug='giant-steps')
        cls.mr_pc = Track.objects.create(name='Mr. PC', slug='mr-pc', album=cls.giant_steps)

    def test_create_solo(self):
        """
        Test that we can create solo
        """
        post_data = {
            'track': '/api/tracks/2/',
            'artist': 'Jhon Coltrane',
            'instrument': 'saxophone',
            'start_time': '0:24',
            'end_time': '3:21'
        }
        solos_url = reverse('api:solo-list')
        response = self.client.post(solos_url, data=post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {
            'url': 'http://testserver/api/solos/1/',
            'artist': 'Jhon Coltrane',
            'slug': 'jhon-coltraine',
            'instrument': 'saxophone',
            'start_time': '0:24',
            'end_time': '3:21',
            'track': 'http://testserver/api/tracks/1/',
        })

    def test_solo_list_route(self):
        """
        Test that we've got routing set up for Solos
        """
        solos_url = reverse('api:solo-list')
        route = resolve(solos_url)
        self.assertEqual(route.func.__name__, 'SoloViewSet')