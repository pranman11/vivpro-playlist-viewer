from rest_framework import serializers
from .models import Rating, Song

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['user', 'song', 'rating']
        read_only_fields = ['user']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
