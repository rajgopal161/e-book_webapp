from unicodedata import name
from django.contrib import admin
from django.urls import path
from cartmgmt import views


app_name = "cartmgmt"

urlpatterns = [
    path('products/<str:book_name>/add_cart',views.add_cart, name="add_cart"),
    path('cart/',views.cart, name="cart"),
    # path('register/register_user',views.register_user, name="register_user"),
    # path('login/',views.loginu, name="login"),
    # path('login/login_user',views.loginuser, name="login_user"),
    # path('logout', views.logoutu, name="logout"),
    # path('user_details', views.userdtls, name='user_details'),
    # path('contact', views.contactus, name='contactus'),
]