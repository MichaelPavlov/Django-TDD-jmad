from django.db.models import QuerySet
from django.test import RequestFactory
from django.test import TestCase

from solos.models import Solo
from solos.views import index


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.drum_solo = Solo.objects.create(
            track='Bugle Call Rag',
            artist='Rich',
            instrument='drums'
        )

        self.bass_solo = Solo.objects.create(
            track='Mr. PC',
            artist='Coltrane',
            instrument='saxophone'
        )

    def test_index_view_basic(self):
        """
        Test that index view returns a 200 response and uses the correct template
        """
        request = self.factory.get('/')
        with self.assertTemplateUsed('solos/index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)

    def test_index_view_returns_solos(self):
        """
        Test that the index view will attempt to return solos if query parameters exist
        """
        response = self.client.get(
            '/',
            {'instrument': 'drums'}
        )
        solos = response.context['solos']

        self.assertIs(type(solos), QuerySet)
        self.assertEqual(len(solos), 1)
        self.assertEqual(solos[0].artist, 'Rich')
