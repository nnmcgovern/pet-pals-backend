from rest_framework import serializers
from .models import Post, Comment, Like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class AllCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [f.name for f in Post._meta.fields] + ['comments'] + ['likes']




class GetAllDogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class GetAllCatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
