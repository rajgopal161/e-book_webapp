from email import message
import re
from django.contrib import messages
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

        if password == password_confirm:
            if UserAuth.objects.filter(username=username).exists():
                print("Username Taken")
                messages.info(request,"Username already Taken")
                return redirect('/register/')
            elif UserAuth.objects.filter(email=email).exists():
                print("Email Taken")
                messages.info(request,"Email already exist")
                return redirect('/register/')
            else:
                user = UserAuth(username=username, email=email, password=password)
                user.save();
                print("user created")
                messages.info(request,"Registered Succesfully, Now login")
                return redirect('/register/')

        else:
            print("Password not matching")
            messages.info(request,"Password not matching")
            return redirect('/register/')
        
        

def login(request):
    return render(request,'myapp/login.html')