from unittest.mock import patch

from django.test import TestCase

from albums.models import Album, Track
from solos.models import Solo


class SoloModelTestCase(TestCase):
    def setUp(self):
        self.album = Album.objects.create(
            name='At the Stratford Shakespearean Festival',
            artist='Oscar Peterson Trio',
            slug='at-the-stratford-shakespearean-festival'
        )

        self.track = Track.objects.create(
            name='Falling in Love with Love',
            album=self.album,
            track_number=1,
            slug='falling-in-love-with-love'
        )

        self.solo = Solo.objects.create(
            track=self.track,
            artist='Oscar Peterson',
            instrument='piano',
            start_time='1:24',
            end_time='4:06',
            slug='oscar-peterson'
        )

    def test_solo_basic(self):
        """
        Test the basic functionality of solo
        """
        self.assertEqual(self.solo.artist, 'Oscar Peterson')
        self.assertEqual(self.solo.end_time, '4:06')

    def test_get_absolute_url(self):
        """
        Test that we can build URL for the solo
        """

        self.assertEqual(self.solo.get_absolute_url(),
                         '/recordings/at-the-stratford-shakespearean-festival/falling-in-love-with-love/oscar-peterson/')

    def test_get_duration(self):
        """
        Test that we can print the duration of a Solo
        """
        self.assertEqual(self.solo.get_duration(), '1:24-4:06')

    @patch('musicbrainzngs.browse_releases')
    @patch('musicbrainzngs.search_artists')
    def test_get_artist_tracks_from_musicbrainz(self, mock_mb_search_artists, mock_mb_browse_releases):
        """
        Test that we can make Solos from the MusicBrainz API
        """
        # mock_mb_search_artists.return_value = {
        #     'artist-list': [
        #         {
        #         'alias-list': [{
        #             'alias': 'Jaco Pastorious',
        #             'sort-name': 'Jaco Pastorious'
        #         }, {
        #             'type': 'Legal name',
        #             'alias': 'John Francis Anthony Pastorius',
        #             'sort-name': 'Pastorius, John Francis Anthony'
        #         }],
        #         'name': 'Jaco Pastorius',
        #         'ipi-list': ['00049970439'],
        #         'gender': 'male',
        #         'area': {
        #             'name': 'United States',
        #             'sort-name': 'United States',
        #             'id': '489ce91b-6658-3307-9877-795b68554c98'
        #         },
        #         'begin-area': {
        #             'name': 'Norristown',
        #             'sort-name': 'Norristown',
        #             'id': '0b345109-5a24-4e47-8bc5-44227f0bdcc3'
        #         },
        #         'type': 'Person',
        #         'ext:score': '100',
        #         'end-area': {
        #             'name': 'Fort Lauderdale',
        #             'sort-name': 'Fort Lauderdale',
        #             'id': 'a2993fdb-6cc6-49da-abe6-831142053fd1'
        #         },
        #         'tag-list': [{
        #             'count': '1',
        #             'name': 'funk'
        #         }, {
        #             'count': '1',
        #             'name': 'jazz fusion'
        #         }, {
        #             'count': '1',
        #             'name': 'jazz'
        #         }, {
        #             'count': '1',
        #             'name': 'american'
        #         }, {
        #             'count': '1',
        #             'name': 'bassist'
        #         }, {
        #             'count': '1',
        #             'name': 'jaco pastorius'
        #         }],
        #         'country': 'US',
        #         'sort-name': 'Pastorius, Jaco',
        #         'life-span': {
        #             'ended': 'true',
        #             'end': '1987-09-21',
        #             'begin': '1951-12-01'
        #         },
        #         'id': '46a6fac0-2e14-4214-b08e-3bdb1cffa5aa'
        #     }, {
        #         'type': 'Group',
        #         'ext:score': '76',
        #         'sort-name': 'Pastorius, Jaco Big Band',
        #         'name': 'Jaco Pastorius Big Band',
        #         'life-span': {
        #             'ended': 'false'
        #         },
        #         'id': 'c403e44b-76f5-40de-937d-e15e3dd9b565'
        #     }, {
        #         'type': 'Group',
        #         'ext:score': '76',
        #         'sort-name': 'Pastorius, Jaco, Trio',
        #         'name': 'Jaco Pastorius Trio',
        #         'life-span': {
        #             'ended': 'false'
        #         },
        #         'id': 'db1e6f90-3918-4ae7-a688-556f03ee9148'
        #     }, {
        #         'sort-name': 'Jaco',
        #         'area': {
        #             'name': 'United Kingdom',
        #             'sort-name': 'United Kingdom',
        #             'id': '8a754a16-0027-3a29-b6d7-2b40ea0481ed'
        #         },
        #         'type': 'Group',
        #         'ext:score': '33',
        #         'name': 'Jaco',
        #         'tag-list': [{
        #             'count': '1',
        #             'name': 'british'
        #         }, {
        #             'count': '1',
        #             'name': 'uk'
        #         }, {
        #             'count': '1',
        #             'name': 'english'
        #         }, {
        #             'count': '1',
        #             'name': 'warp'
        #         }],
        #         'country': 'GB',
        #         'life-span': {
        #             'ended': 'false'
        #         },
        #         'id': '1c72ad30-8c09-4fbf-9f4b-784edc49c1e6'
        #     }, {
        #         'type': 'Person',
        #         'ext:score': '33',
        #         'name': 'Jaco',
        #         'sort-name': 'Jaco',
        #         'disambiguation': 'Polish rapper',
        #         'life-span': {
        #             'ended': 'false'
        #         },
        #         'id': 'f5ad01b9-ceaf-4f95-a9a7-593bf474d9a7'
        #     }, {
        #         'sort-name': 'Jaco',
        #         'area': {
        #             'name': 'Fredrikstad',
        #             'sort-name': 'Fredrikstad',
        #             'id': 'd7916885-2577-4bcc-ae7b-52f2e93df949'
        #         },
        #         'type': 'Person',
        #         'ext:score': '33',
        #         'name': 'Jaco',
        #         'disambiguation': 'Trance/Progressive DJ & producer from Fredrikstad, Norway',
        #         'gender': 'male',
        #         'life-span': {
        #             'ended': 'false',
        #             'begin': '1986-09-21'
        #         },
        #         'id': '6df49a4a-c0bf-4b7b-aa1a-9a3a3190a5a9'
        #     }, {
        #         'ext:score': '33',
        #         'sort-name': 'Jaco',
        #         'name': 'Jaco',
        #         'disambiguation': 'Italo-disco',
        #         'life-span': {
        #             'ended': 'false'
        #         },
        #         'id': 'aef506c9-dc6c-4441-b416-ab176c87f357'
        #     }, {
        #         'sort-name': 'Mary Pastorius',
        #         'area': {
        #             'name': 'United States',
        #             'sort-name': 'United States',
        #             'id': '489ce91b-6658-3307-9877-795b68554c98'
        #         },
        #         'type': 'Person',
        #         'ext:score': '27',
        #         'name': 'Mary Pastorius',
        #         'country': 'US',
        #         'gender': 'female',
        #         'life-span': {
        #             'ended': 'false'
        #         },
        #         'id': '4bfd50f1-96da-4af6-9985-f58b844fbc83'
        #     }, {
        #         'type': 'Person',
        #         'ext:score': '21',
        #         'name': 'Ayesha Jaco',
        #         'sort-name': 'Jaco, Ayesha',
        #         'gender': 'female',
        #         'life-span': {
        #             'ended': 'false'
        #         },
        #         'id': '44dfbdbd-f84b-46b4-ae15-ec39045ac814'
        #     }, {
        #         'life-span': {
        #             'ended': 'false'
        #         },
        #         'ext:score': '20',
        #         'name': 'Jaco Rojzo',
        #         'sort-name': 'Jaco Rojzo',
        #         'id': '75e4f270-8933-4658-bca2-4bb74964e663'
        #     }, {
        #         'type': 'Person',
        #         'ext:score': '19',
        #         'sort-name': 'Loren, Jaco',
        #         'name': 'Jaco Loren',
        #         'life-span': {
        #             'ended': 'false'
        #         },
        #         'id': '04760a50-6de6-4e68-ad66-4d410284ad99'
        #     }, {
        #         'type': 'Person',
        #         'ext:score': '19',
        #         'name': 'Jaco Caraco',
        #         'sort-name': 'Caraco, Jaco',
        #         'tag-list': [{
        #             'count': '1',
        #             'name': 'production music'
        #         }],
        #         'life-span': {
        #             'ended': 'false'
        #         },
        #         'id': '4840333b-0ed8-498a-97e5-045f84fb1a54'
        #     }, {
        #         'type': 'Person',
        #         'ext:score': '19',
        #         'name': 'Jaco Maria',
        #         'sort-name': 'Maria, Jaco',
        #         'disambiguation': 'african jazz artist',
        #         'life-span': {
        #             'ended': 'false'
        #         },
        #         'id': '95791f54-c263-41f3-8c89-828164dfc2e3'
        #     }, {
        #         'sort-name': 'Abel, Jaco',
        #         'area': {
        #             'name': 'Spain',
        #             'sort-name': 'Spain',
        #             'id': '471c46a7-afc5-31c4-923c-d0444f5053a4'
        #         },
        #         'type': 'Person',
        #         'ext:score': '19',
        #         'name': 'Jaco Abel',
        #         'disambiguation': 'Spanish Electric Flamenco Guitar player',
        #         'country': 'ES',
        #         'gender': 'male',
        #         'life-span': {
        #             'ended': 'false',
        #             'begin': '1966'
        #         },
        #         'id': 'fc9b1a41-6209-4783-80a8-1f54b46f406f'
        #     }, {
        #         'sort-name': 'Jaco:neco',
        #         'area': {
        #             'name': 'Japan',
        #             'sort-name': 'Japan',
        #             'id': '2db42837-c832-3c27-b4a3-08198f75693c'
        #         },
        #         'alias-list': [{
        #             'type': 'Artist name',
        #             'alias': '麝香猫',
        #             'sort-name': 'じゃこうねこ'
        #         }],
        #         'type': 'Group',
        #         'ext:score': '19',
        #         'name': 'Jaco:neco',
        #         'country': 'JP',
        #         'life-span': {
        #             'ended': 'true',
        #             'end': '1993',
        #             'begin': '1980'
        #         },
        #         'id': '3d33c0a0-e3f5-405d-a341-9ab1dc36cc84'
        #     }, {
        #         'sort-name': 'Jaco, Wasalu Muhammad',
        #         'area': {
        #             'name': 'United States',
        #             'sort-name': 'United States',
        #             'id': '489ce91b-6658-3307-9877-795b68554c98'
        #         },
        #         'begin-area': {
        #             'name': 'Chicago',
        #             'sort-name': 'Chicago',
        #             'id': '29a709d8-0320-493e-8d0c-f2c386662b7f'
        #         },
        #         'type': 'Person',
        #         'ext:score': '18',
        #         'name': 'Wasalu Muhammad Jaco',
        #         'country': 'US',
        #         'gender': 'male',
        #         'life-span': {
        #             'ended': 'false',
        #             'begin': '1982-02-16'
        #         },
        #         'id': 'ee1a3cdd-d907-4e76-bfe8-f60a8bbd5ba4'
        #     }, {
        #         'life-span': {
        #             'ended': 'false'
        #         },
        #         'ext:score': '16',
        #         'name': 'Jaco & Mixxmaster',
        #         'sort-name': 'Jaco & Mixxmaster',
        #         'id': 'a55b1402-da2f-4c54-8843-49e5fe67375b'
        #     }, {
        #         'name': 'Jacó e Jacozinho',
        #         'area': {
        #             'name': 'Brazil',
        #             'sort-name': 'Brazil',
        #             'id': 'f45b47f8-5796-386e-b172-6c31b009a5d8'
        #         },
        #         'type': 'Group',
        #         'ext:score': '16',
        #         'sort-name': 'Jacó e Jacozinho',
        #         'country': 'BR',
        #         'life-span': {
        #             'ended': 'true',
        #             'end': '1980',
        #             'begin': '1964'
        #         },
        #         'id': '264f8459-d1fb-4b2c-bee8-09c2e271a6f4'
        #     }, {
        #         'name': 'Jaco, der Papagei',
        #         'type': 'Other',
        #         'ext:score': '16',
        #         'sort-name': 'Jaco, der Papagei',
        #         'tag-list': [{
        #             'count': '1',
        #             'name': 'type=animal'
        #         }],
        #         'disambiguation': 'singing parrot',
        #         'life-span': {
        #             'ended': 'false'
        #         },
        #         'id': 'd7fe2327-ea34-4ac7-9bca-0a6ac9fc10d5'
        #     }, {
        #         'name': 'Jaco van Leeuwen',
        #         'type': 'Person',
        #         'ext:score': '16',
        #         'sort-name': 'Leeuwen, Jaco van',
        #         'disambiguation': 'Dutch organist',
        #         'gender': 'male',
        #         'life-span': {
        #             'ended': 'false'
        #         },
        #         'id': '1a8d74f3-ca47-4053-9fd0-6a8f6269e844'
        #     }, {
        #         'ext:score': '16',
        #         'sort-name': 'Merwe, Jaco van der',
        #         'name': 'Jaco van der Merwe',
        #         'disambiguation': 'South African',
        #         'life-span': {
        #             'ended': 'false'
        #         },
        #         'id': 'a7e47bb3-59fc-4b1a-b84b-2aebf0b9fe33'
        #     }, {
        #         'sort-name': 'Steen, Jaco van der',
        #         'area': {
        #             'name': 'Amsterdam',
        #             'sort-name': 'Amsterdam',
        #             'id': 'e8e317a1-268c-4e46-9db1-f10af959ffca'
        #         },
        #         'type': 'Person',
        #         'ext:score': '16',
        #         'name': 'Jaco van der Steen',
        #         'disambiguation': 'Dutch componist, musician',
        #         'gender': 'male',
        #         'life-span': {
        #             'ended': 'false'
        #         },
        #         'id': '1345652f-8879-426c-a7d7-469e201cefc8'
        #     }, {
        #         'type': 'Person',
        #         'ext:score': '13',
        #         'sort-name': 'Largent, Jaco',
        #         'name': 'Jaco Largent',
        #         'life-span': {
        #             'ended': 'false'
        #         },
        #         'id': 'a3b163be-af59-4935-b21c-30389429fe99'
        #     }, {
        #         'sort-name': 'Venter, Jaco',
        #         'area': {
        #             'name': 'South Africa',
        #             'sort-name': 'South Africa',
        #             'id': '50cc7852-862e-30ae-aa82-385fe7135b7f'
        #         },
        #         'type': 'Person',
        #         'ext:score': '13',
        #         'name': 'Jaco Venter',
        #         'tag-list': [{
        #             'count': '1',
        #             'name': 'drums'
        #         }, {
        #             'count': '1',
        #             'name': 'south african'
        #         }],
        #         'disambiguation': 'South African',
        #         'country': 'ZA',
        #         'life-span': {
        #             'ended': 'false'
        #         },
        #         'id': '0394ff8c-05ef-4263-be6a-3782fc44dffc'
        #     }, {
        #         'type': 'Person',
        #         'ext:score': '13',
        #         'sort-name': 'Ayache, Jaco',
        #         'name': 'Jaco Ayache',
        #         'life-span': {
        #             'ended': 'false'
        #         },
        #         'id': '82b267ea-87ff-4449-a51b-f2c78823ad44'
        #     }],
        #     'artist-count': 30
        # }
        # mock_mb_browse_releases.return_value = {}
        mock_mb_search_artists.return_value = {
            'artist-list': [
                {
                    'name': 'Jaco Pastorius',
                    'ext:score': '100',
                    'id': '46a6fac0-2e14-4214-b08e-3bdb1cffa5aa',
                    'tag-list': [
                        {'count': '1', 'name': 'jazz fusion'},
                        {'count': '1', 'name': 'bassist'}
                    ]
                }
            ]
        }

        recording1 = {
            'recording': {
                'id': '12348765-4321-1234-3421-876543210921',
                'title': 'Donna Lee',
            },
            'position': '1'
        }

        recording2 = {
            'recording': {
                'id': '15263748-4321-8765-8765-102938475610',
                'title': 'Sophisticated Lady',
            },
            'position': '6'
        }

        mock_mb_browse_releases.return_value = {
            'release-list': [
                {
                    'title': 'Jaco Pastorius',
                    'id': '876543212-4321-4321-4321-21987654321',
                    'medium-list': [
                        {
                            'track-list': [recording1]
                        }
                    ]
                },
                {
                    'title': 'Invitation',
                    'id': '43215678-5678-4321-1234-901287651234',
                    'medium-list': [
                        {
                            'track-list': [recording2]
                        }
                    ]
                }
            ]
        }
        created_solos = Solo.get_artist_tracks_from_musicbrainz('Jaco Pastorius')
        mock_mb_search_artists.assert_called_with('Jaco Pastorius')
        self.assertEqual(len(created_solos), 2)
        self.assertEqual(created_solos[0].artist, 'Jaco Pastorius')
        self.assertEqual(created_solos[1].track.name, 'Donna Lee')
