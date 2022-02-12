from email import message
import re
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import UserAuth
from myapp.forms import UserAuthForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request,'myapp/index.html' )

def register(request):
    
    return render(request,'myapp/register.html')

def register_user(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password == password_confirm:
            if User.objects.filter(username=username).exists():
                print("Username Taken")
                messages.info(request,"Username already Taken")
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                print("Email Taken")
                messages.info(request,"Email already exist")
                return redirect('/register/')
            else:
                user = User.objects.create_user(first_name=first_name, username=username, email=email, password=password)
                user.save();
                print("user created")
                messages.info(request,"Registered Succesfully, Now login")
                return redirect('/register/')

        else:
            print("Password not matching")
            messages.info(request,"Password not matching")
            return redirect('/register/')
        
        

def loginu(request):
    if request.method == 'POST':
        username = request.POST['username']
        
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("Logged in Succesfully!!")
            
            return redirect('/products/')
        
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('/login/')
    elif request.method== 'GET':
        context={}
    
        return render(request,'myapp/login.html', context)
    

def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("Logged in Succesfully!!")
            print(username)
            return redirect('/products/')
        
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('/login/')

def logoutu(request):
    
    logout(request)
    return redirect('/login/')