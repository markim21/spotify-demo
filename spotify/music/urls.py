from django.urls import path
#from .views import SongView, AlbumView
from music import views

urlpatterns = [
    path("album/", views.create_album),
    path("album/<int:album_id>", views.get_album_by_id),
    path("song/", views.create_song),
    path("songs/", views.get_all_songs)
]