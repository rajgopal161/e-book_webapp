from unicodedata import name
from django.contrib import admin
from django.urls import path
from account import views

app_name = "account"

urlpatterns = [
    path('',views.index, name="index"),
    path('register/',views.register, name="register"),
    path('register/register_user',views.register_user, name="register_user"),
    path('login/',views.login, name="login"),
]