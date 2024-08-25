from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RateSongView, SongViewSet

router = DefaultRouter()
router.register(r'songs', SongViewSet, basename='song')

urlpatterns = [
    path('', include(router.urls)),
    path('rate/', RateSongView.as_view(), name='rate-song'),
]