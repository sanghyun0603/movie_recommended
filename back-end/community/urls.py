from django.urls import path
from . import views


# app_name= 'community'

urlpatterns = [
    path('review/', views.review_list),
    path('review/<int:review_pk>/', views.review_detail),
    path('reviewcomments/', views.review_comment_list),
    path('reviewcomments/<int:comment_pk>/', views.review_comment_detail),
    path('review/<int:review_pk>/reviewcomments/', views.review_comment_create),
    path('reviewlikes/<int:review_pk>/', views.likes_review),

    path('forum/', views.forum_list),
    path('forum/<int:forum_pk>/', views.forum_detail),
    path('forumcomments/', views.forum_comment_list),
    path('forumcomments/<int:comment_pk>/', views.forum_comment_detail),
    path('forum/<int:forum_pk>/forumcomments/', views.forum_comment_create),
    path('forumlikes/<int:forum_pk>/', views.likes_forum),
    
    path('together/', views.together_list),
    path('together/<int:together_pk>/', views.together_detail),
    path('togethercomments/', views.together_comment_list),
    path('togethercomments/<int:comment_pk>/', views.together_comment_detail),
    path('together/<int:together_pk>/togethercomments/', views.together_comment_create),
    path('togetherlikes/<int:together_pk>/', views.likes_together),
]
