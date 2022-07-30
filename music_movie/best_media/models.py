from django.db import models

# Create your models here.

class Song(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    release_date = models.DateTimeField('date published')
    about = models.CharField(max_length=400)
    views = models.IntegerField(default=0)

class Movie(models.Model):
    name = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    release_date = models.DateTimeField('date published')
    about = models.CharField(max_length=400)
    views = models.IntegerField(default=0)
