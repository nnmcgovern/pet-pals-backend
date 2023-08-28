from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from posts.views import PostViewSet, CommentViewSet, LikeViewSet

post_router = routers.DefaultRouter()
post_router.register(r'post', PostViewSet)
post_router.register(r'comment', CommentViewSet)
post_router.register(r'like', LikeViewSet)


urlpatterns = [
    path('', include(post_router.urls)),
    path('admin/', admin.site.urls)
]
