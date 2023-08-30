from django.db import models
from django.contrib.auth.models import User
from posts.models import Comment, Like


class ModelUser(models.Model):
    username = models.CharField()
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.CharField()
    password = models.CharField()
    comments = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='comments')
    like = models.ForeignKey(
        Like, on_delete=models.CASCADE, related_name='like')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
