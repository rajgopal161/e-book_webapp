from unicodedata import name
from django.contrib import admin
from django.urls import path
from myapp import views

app_name = "myapp"

urlpatterns = [
    path('',views.index, name="index"),
    path('products/',views.products, name="products"),
    path('products/book/<str:book_name>/', views.product_detail, name="proddetail"),
    path('products/add_book', views.add_book, name='add_book'),
    path('products/book/<str:book_name>/update/', views.book_update, name='update_name'),
    path('products/book/<str:name>/delete/', views.delete_book, name='delete_book'),
    path('products/book/search/<str:name>', views.search, name="search")
]
