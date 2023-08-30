from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer, LikeSerializer, AllCommentsSerializer
from .models import Post, Comment, Like
from rest_framework.response import Response
from rest_framework import status
from .permissions import CustomPermissions


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().prefetch_related('comments')
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

    def update(self, request, pk=None):
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Response({"detail": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Response({"detail": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)

        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AllCommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = AllCommentsSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [CustomPermissions]
