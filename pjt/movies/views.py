from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, VoteMovie
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .forms import VoteForm
import json
# Create your views here.

def index(request) :
    if request.body:
        jsonObject = json.loads(request.body)
        pageCount = jsonObject.get('pageCount')
        movies = Movie.objects.all()[20*pageCount:20*(pageCount+1)]
        jsonContext = []
        for movie in movies:
            jsonContext.append({
                'pk' : movie.pk,
                'poster_url': movie.poster_path,
                'title': movie.title
            })
        return JsonResponse(jsonContext, safe=False)
    else:
        movies = Movie.objects.all()
        context = {
            'movies': movies[0:20]
        }
        return render(request, 'movies/index.html', context)

def detail(request, movie_pk) :
    movie = Movie.objects.get(pk=movie_pk)
    vote_average = int(movie.vote_average)/2
    director = movie.director
    user = get_object_or_404(get_user_model(), pk=request.user.pk)
    # 유저 평점이 있으면 데이터 전송
    if (VoteMovie.objects.filter(like_movies_id=movie.pk, like_users_id=user.pk).first()):
        uservote = VoteMovie.objects.get(like_movies_id=movie.pk, like_users_id=user.pk).vote
    else:
        uservote = 0
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
        'genres': genres,
        'uservote': uservote
    }
    return render(request, 'movies/detail.html', context)

# 유저 평가 정보 저장
def uservote(request, movie_pk, user_pk):
    jsonObject = json.loads(request.body)
    movie = get_object_or_404(Movie, pk=jsonObject.get('movieId'))
    user = get_object_or_404(get_user_model(), pk=jsonObject.get('userId'))
    vote = jsonObject.get('vote')
    csrfmiddlewaretoken = jsonObject.get('csrftoken')
    vote_values = {
        'vote': vote,
        'csrfmiddlewaretoken': csrfmiddlewaretoken
    }
    form = VoteForm(vote_values)
    if form.is_valid():
        # 별점을 이미 매긴 경우라면
        if VoteMovie.objects.filter(like_movies=movie, like_users=user).exists():
            # 똑같은 별점을 눌렀을 때는 삭제
            if (vote == 0):
                voted = VoteMovie.objects.get(like_movies=movie, like_users=user)
                voted.delete()
                data={}
                return JsonResponse(data)
            # 똑같은 별점이 아닌 별점을 누르면 데이터 갱신
            else:    
                voted = VoteMovie.objects.get(like_movies=movie, like_users=user)
                form = VoteForm(vote_values, instance=voted)
                voted = form.save(commit=False)
                voted.like_movies = movie
                voted.like_users = user
                voted.save()
                context = {}
                return JsonResponse(context)
        # 별점을 처음 매기는 거라면
        else:
            voted = form.save(commit=False)
            voted.like_movies = movie
            voted.like_users = user
            voted.save()
            context = {}
            return JsonResponse(context)
        data={}
        return JsonResponse(data)
    return JsonResponse