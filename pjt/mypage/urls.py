from django.urls import path
from . import views

app_name = "mypage"

urlpatterns = [
    path('<int:user_pk>/profile', views.index, name="index"),
    path('<int:user_pk>/likedirectors', views.likedirectors, name="likedirectors"),
    path('<int:user_pk>/likemovies', views.likemovies, name="likemovies"),
]
