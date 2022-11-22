from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('signin/', views.signin, name="signin"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('<int:user_pk>/update/', views.update, name="update"),
    path('<int:user_pk>/delete/', views.delete, name="delete"),
    path('<int:user_pk>/follow/', views.follow, name="follow"),
    path('<int:user_pk>/password/', views.password, name="password"),
]
