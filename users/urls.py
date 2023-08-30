from django.urls import re_path

from . import views

urlpatterns = [
    re_path('signup',views.sign_up),
    re_path('login',views.login),
    re_path('get_token',views.get_token),
    re_path('get_users',views.get_all_users),
]