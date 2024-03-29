from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path("songs/", views.songs),
    path("movies/", views.movies),
    path('songs/<song_name>', views.song_detail),
    path('movies/<movie_name>', views.movie_detail)
]
