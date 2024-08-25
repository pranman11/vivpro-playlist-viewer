from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from songs.urls import urlpatterns as songs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(songs_urls)),
]
