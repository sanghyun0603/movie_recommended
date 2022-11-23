from rest_framework.response import Response
from rest_framework.decorators import api_view

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import (
    ReviewListSerializer, ReviewSerializer, ReviewCommentSerializer, 
    ForumListSerializer, ForumSerializer, ForumCommentSerializer,
    TogetherListSerializer, TogetherSerializer, TogetherCommentSerializer, 
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
        print(reviews)
        # reviews = get_list_or_404(Review.objects.order_by('-pk'))
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
# 리뷰 상세 페이지 (겟 딜리트 풋)
def review_detail(request, review_pk):
    # review = Review.objects.get(pk=review_pk)
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

##### 22-11-16 수업시간 완료


# 리뷰 댓글 전체 (겟)
@api_view(['GET'])
def review_comment_list(request):
    if request.method == 'GET':
        # comments = ReviewComment.objects.all()
        comments = get_list_or_404(ReviewComment.objects.all())

        serializer = ReviewCommentSerializer(comments, many=True)
        return Response(serializer.data)

# 리뷰 댓글 상세 (겟 딜리트 풋)
@api_view(['GET', 'DELETE', 'PUT'])
def review_comment_detail(request, comment_pk):
    # comment = ReviewComment.objects.get(pk=comment_pk)
    comment = get_object_or_404(ReviewComment, pk=comment_pk)

    if request.method == 'GET':
        serializer = ReviewCommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewCommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# 리뷰 댓글 생성 (포스트)
@api_view(['POST'])
def review_comment_create(request, review_pk):
    # review = Review.objects.get(pk=review_pk)
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user = request.user, review=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 리뷰 좋아요 (포스트)
@api_view(['POST'])
def likes_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    print('**********************************')
    print(request)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    data = review.like_users.all().count()
    # data = str(data)
    return Response(data)
    
        


#########################################
# 자유게시판

# 자유게시판 전체 페이지 (겟 포스트)
@api_view(['GET', 'POST'])
def forum_list(request):
    if request.method == 'GET':
        forums = Forum.objects.order_by('-pk')
        # forums = get_list_or_404(Forum.objects.order_by('-pk'))
        serializer = ForumListSerializer(forums, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ForumSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 자유게시판 상세 페이지 (겟 딜리트 풋)
@api_view(['GET', 'DELETE', 'PUT'])
def forum_detail(request, forum_pk):
    # forum = Forum.objects.get(pk=forum_pk)
    forum = get_object_or_404(Forum, pk=forum_pk)

    if request.method == 'GET':
        serializer = ForumSerializer(forum)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        forum.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ForumSerializer(forum,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 자유게시판 댓글 전체 (겟)
@api_view(['GET'])
def forum_comment_list(request):
    if request.method == 'GET':
        # comments = ForumComment.objects.all()
        comments = get_list_or_404(ForumComment.objects.all())

        serializer = ForumCommentSerializer(comments, many=True)
        return Response(serializer.data)

# 자유게시판 댓글 상세 (겟 딜리트 풋)
@api_view(['GET', 'DELETE', 'PUT'])
def forum_comment_detail(request, comment_pk):
    # comment = ForumComment.objects.get(pk=comment_pk)
    comment = get_object_or_404(ForumComment, pk=comment_pk)

    if request.method == 'GET':
        serializer = ForumCommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ForumCommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


# 자유게시판 댓글 생성 (포스트)
@api_view(['POST'])
def forum_comment_create(request, forum_pk):
    # forum = Forum.objects.get(pk=forum_pk)
    forum = get_object_or_404(Forum, pk=forum_pk)
    serializer = ForumCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # forumcomment = serializer.save(commit=False)
        # forumcomment.user = request.user
        # forumcomment.forum = forum
        serializer.save(user = request.user, forum=forum)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def likes_forum(request, forum_pk):
    forum = get_object_or_404(Forum, pk=forum_pk)
    if forum.like_users.filter(pk=request.user.pk).exists():
        forum.like_users.remove(request.user)
    else:
        forum.like_users.add(request.user)
    data = forum.like_users.all().count()
    # data = str(data)
    return Response(data)

#########################################
# 모여요

# 모여요 전체 페이지 (겟 포스트)
@api_view(['GET', 'POST'])
def together_list(request):
    if request.method == 'GET':
        together = Together.objects.order_by('-pk')
        # together = get_list_or_404(Together.objects.order_by('-pk'))
        serializer = TogetherListSerializer(together, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TogetherSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 모여요 상세 페이지 (겟 딜리트 풋)
@api_view(['GET', 'DELETE', 'PUT'])
def together_detail(request, together_pk):
    # together = Together.objects.get(pk=together_pk)
    together = get_object_or_404(Together, pk=together_pk)
    if request.method == 'GET':
        serializer = TogetherSerializer(together)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        together.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = TogetherSerializer(together,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 모여요 댓글 전체 (겟)
@api_view(['GET'])
def together_comment_list(request):
    if request.method == 'GET':
        # comments = TogetherComment.objects.all()
        comments = get_list_or_404(TogetherComment.objects.all())

        serializer = TogetherCommentSerializer(comments, many=True)
        return Response(serializer.data)


# 모여요 댓글 상세 (겟 딜리트 풋)
@api_view(['GET', 'DELETE', 'PUT'])
def together_comment_detail(request, comment_pk):
    # comment = TogetherComment.objects.get(pk=comment_pk)
    comment = get_object_or_404(TogetherComment, pk=comment_pk)

    if request.method == 'GET':
        serializer = TogetherCommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = TogetherCommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
# 모여요 댓글 생성 (포스트)
@api_view(['POST'])
def together_comment_create(request, together_pk):
    # together = Together.objects.get(pk=together_pk)
    together = get_object_or_404(Together, pk=together_pk)

    serializer = TogetherCommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user = request.user, together=together)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def likes_together(request, together_pk):
    together = get_object_or_404(Together, pk=together_pk)
    if together.like_users.filter(pk=request.user.pk).exists():
        together.like_users.remove(request.user)
    else:
        together.like_users.add(request.user)
    data = together.like_users.all().count()
    # data = str(data)
    return Response(data)