from django.db import models
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import User, Permission, AbstractUser
from django.contrib.contenttypes.models import ContentType


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


# class CustomUserManager(UserManager):
#     def _create_user(self, username, email, password, **extra_fields):
#         extra_fields.setdefault('is_active', True)
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)

#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)

#         # Add the delete permission to the user
#         content_type = ContentType.objects.get_for_model(user)
#         delete_permission = Permission.objects.get(
#             codename='delete_user', content_type=content_type)
#         user.user_permissions.add(delete_permission)

#         return user


# class CustomUser(AbstractUser):
#     # Your custom fields here

#     objects = CustomUserManager()
