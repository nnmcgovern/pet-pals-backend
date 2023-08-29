from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer, LikeSerializer, GetAllDogsSerializer, GetAllCatsSerializer
from .models import Post, Comment, Like

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response

from .permissions import CustomPermissions

# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class GetAllDogsCatsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, methods=['GET'])
    def dogs(self, request):
        dogs = self.queryset.filter(animal_type='Dog')
        serializer = PostSerializer(dogs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def cats(self, request):
        cats = self.queryset.filter(animal_type='Cat')
        serializer = PostSerializer(cats, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CustomPermissions]


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
