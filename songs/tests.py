from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Song, Rating

class SongAPITests(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Create a user for authentication
        cls.user = User.objects.create_user(username='testuser', password='testpass')

        # Create some songs
        cls.songs = [
            Song.objects.create(
                id=f'song{i}',
                title=f'Song {i}',
                danceability=0.5,
                energy=0.5,
                key=1,
                loudness=-5,
                mode=1,
                acousticness=0.1,
                instrumentalness=0.0,
                liveness=0.1,
                valence=0.5,
                tempo=120,
                duration_ms=200000,
                time_signature=4,
                num_bars=10,
                num_sections=5,
                num_segments=50,
                song_class=1
            ) for i in range(1, 6)
        ]
        
    def test_list_songs(self):
        """
        Ensure we can list all songs with pagination.
        """
        url = reverse('song-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
        self.assertEqual(len(response.data['results']), 5)
        
    def test_rate_song(self):
        """
        Ensure we can rate a song.
        """
        song = self.songs[0]
        url = reverse('rate-song')
        self.client.force_authenticate(user=self.user)
        data = {'song': song.pk, 'rating': 4}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Rating.objects.count(), 1)
        self.assertEqual(Rating.objects.get().rating, 4)

    def test_retrieve_song_by_title(self):
        """
        Ensure we can retrieve a song by its title.
        """
        song = self.songs[0]
        url = reverse('song-retrieve-by-title') + f'?title={song.title}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], song.title)
        self.assertEqual(response.data['id'], song.id)
