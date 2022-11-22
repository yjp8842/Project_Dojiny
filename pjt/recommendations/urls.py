from django.urls import path
from . import views

app_name = 'recommendations'
urlpatterns = [
    path('<int:user_pk>/rec/', views.index, name="index"), 
]
