from rest_framework.response import Response
from rest_framework.decorators import api_view

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieSerializer, ActorSerializer, GenreSerializer
from .models import Movie, Genre, Actor

# 영화 리스트
@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        # movies = get_list_or_404(Movie.objects.order_by('-pk'))
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
# 영화 상세
@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)



# 배우
@api_view(['GET'])
def actor_list(request):
    if request.method == 'GET':
        actors = Actor.objects.all()
        # movies = get_list_or_404(Actor.objects.order_by('-pk'))
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)

# 장르
@api_view(['GET'])
def genre_list(request):
    if request.method == 'GET':
        genre = Genre.objects.all()
        # genre = get_list_or_404(Genre.objects.order_by('-pk'))
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)