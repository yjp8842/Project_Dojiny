from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import get_user_model

from django.http import JsonResponse

import json

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
    if request.body:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        movies = person.votemovie_set.all()
        jsonObject = json.loads(request.body)
        stars = jsonObject.get('stars')
        starList = float(jsonObject.get('starList'))
        starsList = jsonObject.get('starsList')
        returnlist = 0
        status = ''
        moviesstarlist = movies.filter(vote=stars).count()
        if moviesstarlist / 5 <= starList :
            returnlist = moviesstarlist // 5
            status = 'over'
        else:
            status = 'none'
            returnlist = starList

        moviesanystar = movies.filter(vote=stars)[5*returnlist:5*(returnlist+1)]
        jsonContext = []
        for movie in moviesanystar:
            jsonContext.append({
                'poster_url': movie.like_movies.poster_path,
                'title': movie.like_movies.title,
                'status': status,
                'returnstarlist': starsList
            })
        return JsonResponse(jsonContext, safe=False)
    else:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        movies = person.votemovie_set.all()
        movies5star = movies.filter(vote=5)[0:5]
        movies4star = movies.filter(vote=4)[0:5]
        movies3star = movies.filter(vote=3)[0:5]
        movies2star = movies.filter(vote=2)[0:5]
        movies1star = movies.filter(vote=1)[0:5]
        context = {
            'person': person,
            'movies5star': movies5star,
            'movies4star': movies4star,
            'movies3star': movies3star,
            'movies2star': movies2star,
            'movies1star': movies1star,
        }
        return render(request, 'mypage/likemovies.html', context)