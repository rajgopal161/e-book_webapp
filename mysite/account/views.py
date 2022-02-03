from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import UserAuth
from myapp.forms import UserAuthForm

# Create your views here.

def index(request):
    return render(request,'myapp/index.html' )

def register(request):


    return render(request,'myapp/register.html')

def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        user = UserAuth(username=username, email=email, password=password)
        user.save();
        print("user created")
        return redirect('/login/')

def login(request):
    return render(request,'myapp/login.html')