from django.db import models
import datetime


class Post(models.Model):
    name = models.CharField()
    image = models.CharField()
    age = models.IntegerField()
    animal_type = models.CharField()
    breed = models.CharField()
    description = models.CharField()
    gender = models.CharField()
    owner_id = models.IntegerField()
    created_at = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.CharField()
    user_id = models.IntegerField()
    post_id = models.IntegerField()
    updated_at = models.DateField(default=datetime.date.today)
    created_at = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.text


class Like(models.Model):
    user_id = models.CharField()
    post_id = models.CharField()

    def __str__(self):
        return 'Like'
