from django.shortcuts import render
from django.http import HttpResponse
from .models import Song, Movie


# Create your views here.

def welcome(request):
    # return HttpResponse("Welcome to the best ever MediaWorld.")
    return render(request, 'best_media/welcome.html')


def songs(request):
    song_list = Song.objects.all()
    return render(request, 'best_media/song.html', {'song_list': song_list})

def movies(request):
    movie_list = Movie.objects.all()
    return render(request, 'best_media/movie.html', {'movie_list': movie_list})


def song_detail(request, song_name):
    song = Song.objects.get(name=song_name)
    song.views += 1
    song.save()
    return render(request, 'best_media/song_detail.html', {'song': song})


def movie_detail(request, movie_name):
    movie = Movie.objects.get(name=movie_name)
    movie.views += 1
    movie.save()
    return render(request, 'best_media/movie_detail.html', {'movie': movie})


