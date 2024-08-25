from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg, Count

class Song(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255)
    danceability = models.FloatField()
    energy = models.FloatField()
    key = models.PositiveSmallIntegerField()
    loudness = models.FloatField()
    mode = models.PositiveSmallIntegerField()
    acousticness = models.FloatField()
    instrumentalness = models.FloatField()
    liveness = models.FloatField()
    valence = models.FloatField()
    tempo = models.FloatField()
    duration_ms = models.BigIntegerField()
    time_signature = models.IntegerField()
    num_bars = models.IntegerField()
    num_sections = models.IntegerField()
    num_segments = models.IntegerField()
    song_class = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('user', 'song')

    def __str__(self):
        return f"{self.user.username} rated {self.song.title} as {self.rating} stars"

