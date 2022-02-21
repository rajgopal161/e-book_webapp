from unicodedata import name
from django.contrib import admin
from django.urls import path
from account import views


app_name = "account"

urlpatterns = [
    path('',views.index, name="index"),
    path('register/',views.register, name="register"),
    path('register/register_user',views.register_user, name="register_user"),
    path('login/',views.loginu, name="login"),
    path('login/login_user',views.loginuser, name="login_user"),
    path('logout', views.logoutu, name="logout"),
    path('user_details', views.userdtls, name='user_details'),
    path('contact', views.contactus, name='contactus'),
]