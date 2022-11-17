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
    genres = []
    sub_stack = ''
    for g in movie.genres:
        if g.isalpha():
            sub_stack += g
        elif sub_stack:
            genres.append(sub_stack)
            sub_stack = ''
    context = {
        'movie': movie,
        'vote_average': vote_average,
        'director': director,
        'genres': genres
    }
    return render(request, 'movies/detail.html', context)