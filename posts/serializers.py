from rest_framework import serializers
from .models import Post, Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [f.name for f in Post._meta.fields] + ['comments']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class GetAllDogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class GetAllCatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
