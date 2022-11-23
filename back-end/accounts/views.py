from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import update_session_auth_hash, get_user_model
from .models import User
from .serializers import CustomRegisterSerializer,AccountsSerializer
from community.serializers import ForumListSerializer, ReviewListSerializer, TogetherListSerializer
from movies.serializers import MovieSerializer
# Create your views here.
@api_view(['DELETE'])
def withdrawal(request):
    if request.method == 'DELETE':
        user = get_object_or_404(get_user_model(),pk=request.user.pk)
        user.delete()
    return Response('check')

@api_view(['GET'])
def getnowuesrinfo(request):
    if request.method =='GET':
        user = get_object_or_404(get_user_model(),pk=request.user.pk)
        serializer = AccountsSerializer(user)
        return Response(serializer.data)


@api_view(['GET'])
def getuserinfo(request, username):
    if request.method == 'GET':
        user = get_object_or_404(get_user_model(),username=username)
        serializer = CustomRegisterSerializer(user)
        return Response(serializer.data)   

@api_view(['GET'])
def userlikesforum(request, username):
    if request.method == 'GET':
        user = get_object_or_404(get_user_model(),username=username)
        forums = user.like_forum.all()
            
        serializer = ForumListSerializer(forums, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def userlikesreview(request, username):
    if request.method == 'GET':
        user = get_object_or_404(get_user_model(),username=username)
        reviews = user.like_review.all()
            
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def userlikestogether(request, username):
    if request.method == 'GET':
        user = get_object_or_404(get_user_model(),username=username)
        togethers = user.like_together.all()
            
        serializer = TogetherListSerializer(togethers, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def userlikesmovie(request, username):
    if request.method == 'GET':
        user = get_object_or_404(get_user_model(),username=username)
        movies = user.like_movies.all()
            
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)