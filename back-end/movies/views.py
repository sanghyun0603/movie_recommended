from rest_framework.response import Response
from rest_framework.decorators import api_view

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieSerializer, ActorSerializer, GenreSerializer
from .models import Movie, Genre, Actor
import random
# 영화 좋아요
@api_view(['POST'])
def likes_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    data = movie.like_users.all().count()
    # data = str(data)
    return Response(data)

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

# 영화 추천 알고리즘
@api_view(['POST'])
def movie_recommend(request):
    print('영화 추천 알고리즘')
    selectedgenres = request.data
    search_genres = Genre.objects.all()
    show_genres = []
    for select in selectedgenres:
        for search_genre in search_genres:
            if search_genre.id == select:
                show_genres.append(search_genre.name)
    moviesss = Movie.objects.all()
    moviesss = list(moviesss)
    movies = random.sample(moviesss,2000)
    
    #==============================================
    # 장르별 알고리즘부분 =========================
    genre_movies_coll = []
    for selgenre in selectedgenres:
        genre_movies = []
        for movie in movies:
            for genre in movie.genres.all():
                if genre.id == selgenre:
                    genre_movies.append(movie)
        random_genre_movies = random.sample(genre_movies,20)
        genre_movies_coll.append(random_genre_movies)
    
    #==============================================

    # 최고 추천 영화 부분 =========================
    reco = []
    plus_rate = [30,25,20,15,10]
    for movie in movies:
        cnt = 0
        for genre in movie.genres.all():
            for i, selectedgenre in enumerate(selectedgenres):
                if genre.id == selectedgenre:
                    cnt += plus_rate[i]
        if cnt > 0:
            reco.append([movie,cnt,movie.vote_average])
    reco.sort(key=lambda x: (-x[1], -x[2]))
    # print(reco)
    best_reco = []
    for obj,count,vote in reco:
        best_reco.append(obj)
    best_reco = list(set(best_reco[:15]))
    #===============================================
    serializer_best =  MovieSerializer(best_reco, many=True)
    serializers =[serializer_best.data]
    for i in range(len(genre_movies_coll)):
        globals()['serializer_'+str(i)] = MovieSerializer(genre_movies_coll[i], many=True)
        serializers.append(globals()['serializer_'+str(i)].data)
    serializers.append(show_genres)
    return Response(serializers)


# 영화 검색
@api_view(['POST'])
def movie_search(request):
    movie_title = request.data.get('movie_name')

    movies = Movie.objects.filter(title__contains = movie_title)

    serializer =  MovieSerializer(movies, many=True)
    return Response(serializer.data)



# 배우
@api_view(['GET'])
def actor_list(request):
    if request.method == 'GET':
        actors = Actor.objects.all()
        # movies = get_list_or_404(Actor.objects.order_by('-pk'))
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)

# 영화별 배우
@api_view(['POST'])
def movie_recommend_actor(request):
    movie_id = request.data.get('movieId')
    movies = Movie.objects.all()
    for movie in movies:
        if int(movie_id) == movie.id:
            select_movie = movie
            break
    actor = []
    all_actors = select_movie.actors.all()
    for all_actor in all_actors:
        actor.append(all_actor)
    serializer = ActorSerializer(actor, many=True)
    return Response(serializer.data)

# 영화별 장르
@api_view(['POST'])
def movie_recommend_genre(request):
    movie_id = request.data.get('movieId')
    movie_id = int(movie_id)
    # movies = Movie.objects.all()
    # for movie in movies:
    #     if int(movie_id) == movie.id:
    #         select_movie = movie
    #         break
    select_movie = Movie.objects.get(pk=movie_id)
    genre = []
    all_genres = select_movie.genres.all()
    for all_genre in all_genres:
        genre.append(all_genre)
    serializer = ActorSerializer(genre, many=True)
    return Response(serializer.data)

# 장르
@api_view(['GET'])
def genre_list(request):
    if request.method == 'GET':
        genre = Genre.objects.all()
        # genre = get_list_or_404(Genre.objects.order_by('-pk'))
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)
