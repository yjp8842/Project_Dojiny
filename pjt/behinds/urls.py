from django.urls import path
from . import views

app_name = "behinds"

urlpatterns = [
     path('', views.index, name="index"),
     path('create/', views.create, name="create"),
     path('<int:behind_pk>/detail/', views.detail, name="detail"),
     path('<int:behind_pk>/delete/', views.delete, name="delete"),
     path('<int:behind_pk>/update/', views.update, name="update"),
     path('<int:behind_pk>/comment_create/', views.comment_create, name="comment_create"),
     path('<int:behind_pk>/comment_update/<int:comment_pk>/', views.comment_update, name="comment_update"),
     path('<int:behind_pk>/comment_delete/<int:comment_pk>/', views.comment_delete, name="comment_delete"),
     path('<int:behind_pk>/likes/', views.likes, name="likes"),
]
