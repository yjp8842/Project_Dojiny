from django.db import models
from django.conf import settings
# Create your models here.

class Movie(models.Model) :
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    
    genres = models.CharField(max_length=200)
    movie_id = models.IntegerField()
    original_title = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    overview = models.CharField(max_length=50)
    release_date = models.CharField(max_length=50)
    vote_average = models.IntegerField()
    director = models.CharField(max_length=50)
    poster_path = models.CharField(max_length=50)
    backdrop_path = models.CharField(max_length=50)
    runtime = models.IntegerField()