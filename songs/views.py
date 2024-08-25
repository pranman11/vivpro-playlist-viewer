import json
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .models import Song, Rating
from .serializers import RatingSerializer, SongSerializer

# API view to handle song rating
class RateSongView(CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        song_id = request.data.get('song')
        
        try:
            rating_value = int(request.data.get('rating'))
            if rating_value < 1 or rating_value > 5:
                return Response({"error": "Rating must be 1, 2, 3, 4, or 5"}, status=status.HTTP_400_BAD_REQUEST)
                
            song = Song.objects.get(id=song_id)
        except ValueError:
            return Response({"error": "Rating must be 1, 2, 3, 4, or 5"}, status=status.HTTP_400_BAD_REQUEST)
        except Song.DoesNotExist:
            return Response({"error": "Song not found"}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user has already rated this song
        rating, created = Rating.objects.update_or_create(
            user=user,
            song=song,
            defaults={'rating': rating_value},
        )

        if created:
            return Response({"message": "Rating created successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Rating updated successfully"}, status=status.HTTP_200_OK)
        

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    @action(detail=False, methods=['get'], url_path='by-title')
    def retrieve_by_title(self, request):
        """
        Custom action to retrieve a song by its title.
        """
        title = request.query_params.get('title', None)
        if not title:
            return Response({"error": "Title parameter is missing"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            song = Song.objects.get(title=title)
        except Song.DoesNotExist:
            return Response({"error": "Song not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)
