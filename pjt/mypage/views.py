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
        'directors': directors
    }
    return render(request, 'mypage/likedirectors.html', context)

def likemovies(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    pass
    return render(request, 'mypage/likedirectors.html')