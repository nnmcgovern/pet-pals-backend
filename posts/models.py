from django.db import models


class Post(models.Model):
    name = models.CharField()
    image = models.CharField()
    age = models.IntegerField()
    animal_type = models.CharField()
    breed = models.CharField()
    description = models.CharField()
    gender = models.CharField()
    owner_id = models.IntegerField()


class Comment(models.Model):
    text = models.CharField()
    date_created = models.DateField()
    user_id = models.IntegerField()
    post_id = models.IntegerField()


class Like(models.Model):
    user_id = models.CharField()
    post_id = models.CharField()
