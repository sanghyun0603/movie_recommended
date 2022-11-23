from rest_framework import serializers
from .models import Review , Forum, ReviewComment, ForumComment, Together, TogetherComment

# - ReviewListSerializer - get,post (리뷰 게시판 전체 조회, 글 작성)
class ReviewListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    nickname = serializers.CharField(source='user.nickname', read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'title', 'nickname','user_id','username','poster_path','movie_title','created_at','score')

# - ReviewCommentSerializer - get,post,del,put (리뷰 게시판 댓글 조회, 생성, 삭제, 수정)
class ReviewCommentSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    
    class Meta:
        model = ReviewComment
        fields = '__all__'
        read_only_fields = ('review','user',)

# - ReviewSerializer - get,put,del (리뷰 게시판 상세 조회, 수정, 삭제)
class ReviewSerializer(serializers.ModelSerializer):
    
    reviewcomment_set = ReviewCommentSerializer(many=True, read_only=True)
    nickname = serializers.CharField(source='user.nickname', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user','like_users')


# - ForumListSerializer -get,post (자유 게시판 전체 조회, 글 작성)
class ForumListSerializer(serializers.ModelSerializer):
    # 현재 로그인 한 유저 네임 알기 위해서
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Forum
        fields = ('id', 'title', 'nickname','user_id','username','created_at')

# - ForumCommentSerializer -get,post,delete,put (자유 게시판 댓글 조회, 생성, 삭제, 수정)
class ForumCommentSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname', read_only=True)

    class Meta:
        model = ForumComment
        fields = '__all__'
        read_only_fields = ('forum','user',)

# - ForumSerializer - get,put,delete (자유 게시판 상세 조회, 수정, 삭제)
class ForumSerializer(serializers.ModelSerializer):
    
    forumcomment_set = ForumCommentSerializer(many=True, read_only=True)
    nickname = serializers.CharField(source='user.nickname', read_only=True)

    class Meta:
        model = Forum
        fields = '__all__'
        read_only_fields = ('user','like_users')

# - TogetherListSerializer - get,post (모임 게시판 전체 조회, 글 작성)
class TogetherListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    nickname = serializers.CharField(source='user.nickname', read_only=True)

    class Meta:
        model = Together
        fields = ('id', 'title', 'nickname','endtime','user_id','username','created_at')

# - TogetherCommentSerializer - get,post,del,put (모임 게시판 댓글 조회, 생성, 삭제, 수정)
class TogetherCommentSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname', read_only=True)

    class Meta:
        model = TogetherComment
        fields = '__all__'
        read_only_fields = ('together','user',)

# - TogetherSerializer - get,put,del (모임 게시판 상세 조회, 수정, 삭제)
class TogetherSerializer(serializers.ModelSerializer):
    
    togethercomment_set = TogetherCommentSerializer(many=True, read_only=True)
    nickname = serializers.CharField(source='user.nickname', read_only=True)

    class Meta:
        model = Together
        fields = '__all__'
        read_only_fields = ('user','like_users')

