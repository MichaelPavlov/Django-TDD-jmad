from django.db.models import QuerySet
from django.test import RequestFactory
from django.test import TestCase

from solos.models import Solo
from solos.views import index, SoloDetailView


class SolosBaseTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.drum_solo = Solo.objects.create(
            track='Bugle Call Rag',
            artist='Rich',
            instrument='drums'
        )

        cls.bass_solo = Solo.objects.create(
            track='Mr. PC',
            artist='Coltrane',
            instrument='saxophone'
        )


class IndexViewTestCase(SolosBaseTestCase):
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


class SoloViewTestCase(SolosBaseTestCase):
    def test_basic(self):
        """
        Test that the solo view returns 200 response, uses the correct template and has the correct context
        """

        request = self.factory.get('/solos/1/')

        # print()
        response = SoloDetailView.as_view()(
            request,
            pk=self.drum_solo.pk
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['solo'].artist, 'Rich')

        with self.assertTemplateUsed('solos/solo_detail.html'):
            response.render()
