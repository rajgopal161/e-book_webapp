from django.shortcuts import render, redirect
from myapp.models import Book
from django.contrib import messages

# Create your views here.

def payment_details(request):
    #messages.info(request,"Please enter valid Debit/Credit card")
    return render(request, "myapp/cards.html")