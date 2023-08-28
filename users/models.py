from django.db import models


class User(models.Model):
    username = models.CharField()
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.CharField()
    password = models.CharField()
