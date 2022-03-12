from django.shortcuts import render, redirect
from myapp.models import Book

# Create your views here.

def payment_details(request):
    return render(request, "myapp/cards.html")