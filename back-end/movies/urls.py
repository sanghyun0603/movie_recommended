from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list,),
    path('actors/', views.actor_list,),
    path('genres/', views.genre_list,),
]
