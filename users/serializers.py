from rest_framework import serializers
from posts.serializers import CommentSerializer, LikeSerializer
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    class Meta(object):
        model = User
        fields = ['id','username', 'password', 'email', 'first_name', 'last_name', 'comments', 'likes']
