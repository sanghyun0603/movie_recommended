from rest_framework import serializers
from .models import Genre, Movie, Actor

#Movie
class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


# class DicMovie(object):
#     def __init__(self, dictionary):
#         self.dict = dictionary

# class GenreMovieSerializer(serializers.Serializer):
#     dictionary = serializers.DictField(
#     child = serializers.CharField()
#     )

#Actor
class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'

#Genre
class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'