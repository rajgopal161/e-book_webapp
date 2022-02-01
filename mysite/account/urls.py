from unicodedata import name
from django.contrib import admin
from django.urls import path
from account import views

app_name = "account"

urlpatterns = [
    path('index/',views.index, name="index"),
    path('index/register/',views.register, name="register"),
    path('index/login/',views.login, name="login"),
]