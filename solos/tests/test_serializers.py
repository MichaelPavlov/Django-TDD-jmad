from django.test import TestCase

from solos.api.serializers import SoloSerializer


class SoloSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_validate(self):
        """
        Test that SoloSerializer.validate() adds a slugged version of the artist attribute to the data
        """
        serializer = SoloSerializer()
        data = serializer.validate({'artist': 'Ray Brown'})
        self.assertEqual(data, {
            'artist': 'Ray Brown',
            'slug': 'ray-brown'
        })
