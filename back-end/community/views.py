from rest_framework.response import Response
from rest_framework.decorators import api_view

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import (
    ForumListSerializer, ForumSerializer, ForumCommentSerializer,
    ReviewListSerializer, ReviewCommentSerializer, ReviewSerializer,
    TogetherListSerializer, TogetherCommentSerializer, TogetherSerializer,
)
from .models import  (
    Review, ReviewComment,
    Forum, ForumComment,
    Together, TogetherComment,
)
#######################################
# 리뷰

# 리뷰 전체 페이지 (겟 포스트)
@api_view(['GET', 'POST'])
def review_list(request):
    if request.method == 'GET':
        reviews = Review.objects.order_by('-pk')
        serializer = ForumListSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ForumSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
# 리뷰 상세 페이지 (겟 딜리트 풋)
def review_detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'GET':
        serializer = ForumSerializer(review, many=True)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ForumSerializer(review, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

##### 22-11-16 수업시간 완료


# 리뷰 댓글 전체 (겟)
@api_view(['GET'])
def review_comment_list(request):
    if request.method == 'GET':
          pass

# 리뷰 댓글 상세 (겟 딜리트 풋)
@api_view(['GET', 'DELETE', 'PUT'])
def review_comment_detail(request):
    if request.method == 'GET':
          pass
    elif request.method == 'DELETE':
        pass
    elif request.method == 'PUT':
        pass

# 리뷰 댓글 생성 (포스트)
@api_view(['POST'])
def review_comment_detail(request):
    if request.method == 'POST':
          pass

#########################################
# 자유게시판

# 자유게시판 전체 페이지 (겟 포스트)
@api_view(['GET', 'POST'])
def forum_list(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass


# 자유게시판 상세 페이지 (겟 딜리트 풋)
@api_view(['GET', 'DELETE', 'PUT'])
def forum_detail(request):
    if request.method == 'GET':
          pass
    elif request.method == 'DELETE':
        pass
    elif request.method == 'PUT':
        pass

# 자유게시판 댓글 전체 (겟)
@api_view(['GET'])
def forum_comment_list(request):
    if request.method == 'GET':
          pass

# 자유게시판 댓글 상세 (겟 딜리트 풋)
@api_view(['GET', 'DELETE', 'PUT'])
def forum_comment_detail(request):
    if request.method == 'GET':
          pass
    elif request.method == 'DELETE':
        pass
    elif request.method == 'PUT':
        pass

# 자유게시판 댓글 생성 (포스트)
@api_view(['POST'])
def forum_comment_detail(request):
    if request.method == 'POST':
          pass

#########################################
# 모여요

# 모여요 전체 페이지 (겟 포스트)
@api_view(['GET', 'POST'])
def together_list(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass

# 모여요 상세 페이지 (겟 딜리트 풋)
@api_view(['GET', 'DELETE', 'PUT'])
def together_detail(request):
    if request.method == 'GET':
          pass
    elif request.method == 'DELETE':
        pass
    elif request.method == 'PUT':
        pass

# 모여요 댓글 전체 (겟)
@api_view(['GET'])
def together_comment_list(request):
    if request.method == 'GET':
        pass

# 모여요 댓글 상세 (겟 딜리트 풋)
@api_view(['GET', 'DELETE', 'PUT'])
def together_comment_detail(request):
    if request.method == 'GET':
          pass
    elif request.method == 'DELETE':
        pass
    elif request.method == 'PUT':
        pass
    
# 모여요 댓글 생성 (포스트)
@api_view(['POST'])
def together_comment_detail(request):
    if request.method == 'POST':
          pass