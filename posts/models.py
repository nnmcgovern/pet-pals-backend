from django.db import models
from django.contrib.auth.models import User
import datetime


class Post(models.Model):
    name = models.CharField()
    image = models.CharField()
    age = models.IntegerField()
    animal_type = models.CharField()
    breed = models.CharField()
    description = models.CharField()
    gender = models.CharField()
    owner_id = models.ForeignKey(
        User, on_delete=models.CASCADE)
    created_at = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.CharField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE)
    updated_at = models.DateField(default=datetime.date.today)
    created_at = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.text


class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE)

    def __str__(self):
        return 'Like'
