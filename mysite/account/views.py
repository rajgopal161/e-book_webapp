from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'myapp/index.html' )

def register(request):
    return render(request,'myapp/register.html')

def login(request):
    return render(request,'myapp/login.html')