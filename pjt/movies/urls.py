from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name="index"), 
    path('<int:movie_pk>/detail/', views.detail, name="detail"), 
    path('<int:movie_pk>/detail/<int:user_pk>/uservote', views.uservote, name="uservote"), 
]
