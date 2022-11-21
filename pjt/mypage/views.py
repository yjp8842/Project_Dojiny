from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import get_user_model
# Create your views here.

def index(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    context = {
        'person': person,
    }
    return render(request, 'mypage/index.html', context)

def likedirectors(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    directors = person.followings.all()
    context = {
        'person' : person,
        'directors': directors
    }
    return render(request, 'mypage/likedirectors.html', context)

def likemovies(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    movies = person.votemovie_set.all()
    movies5star = movies.filter(vote=5)
    movies4star = movies.filter(vote=4)
    movies3star = movies.filter(vote=3)
    movies2star = movies.filter(vote=2)
    movies1star = movies.filter(vote=1)
    context = {
        'person': person,
        'movies5star': movies5star,
        'movies4star': movies4star,
        'movies3star': movies3star,
        'movies2star': movies2star,
        'movies1star': movies1star,
    }
    return render(request, 'mypage/likemovies.html', context)