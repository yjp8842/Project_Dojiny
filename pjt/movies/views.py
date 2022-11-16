from django.shortcuts import render
from .models import Movie
# Create your views here.

def index(request) :
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)

def detail(request, movie_pk) :
    movie = Movie.objects.get(pk=movie_pk)
    vote_average = int(movie.vote_average)/2
    director = movie.director
    context = {
        'movie': movie,
        'vote_average': vote_average,
        'director': director,
    }
    return render(request, 'movies/detail.html', context)