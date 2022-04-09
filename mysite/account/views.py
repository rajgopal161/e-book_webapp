from email import message
import re
from urllib import request
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import UserAuth
from myapp.forms import UserAuthForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import send_mail

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
                
                
                #Sending email after successful registration.

                # subject = 'Welcome to E-commerce Book Store'
                # message = f'Hi {user.username}, Thank You for registering with E-commerce Book Store'
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list = [user.email, ]
                # send_mail( subject, message, email_from, recipient_list )
                # print("Email Sent Succesfully!!")

                user.save();
                print("user created")
                messages.info(request,"Registered Succesfully, Now login")
                return redirect('/register/')

        else:
            print("Password not matching")
            messages.info(request,"Password not matching")
            return redirect('/register/')
        
        

def loginu(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
        
    #     password = request.POST['password']

    #     user = authenticate(request, username=username, password=password)

    #     if user is not None:
    #         login(request, user)
    #         print("Logged in Succesfully!!")
            
    #         return redirect('/products/')
        
    #     else:
    #         messages.info(request,"Invalid Credentials")
    #         return redirect('/login/')
    if request.method== 'GET':
        
    
        return render(request,'myapp/login.html')
    

def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            request.session['user_id'] = request.user.id
            request.session['email'] = request.user.email

            print("Logged in Succesfully!!")
            print("You are : ", request.session.get('email'))
            return redirect('/products/')
        
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('/login/')

def logoutu(request):
    
    logout(request)
    return redirect('/login/')

def userdtls(request):
    return render(request, 'myapp/user_details.html')

def contactus(request):
    return render(request, 'myapp/contactus.html')

def passupdate(request):
    return render(request, 'myapp/updatepass.html')


def updatepswd(request):
    if request.method == 'POST':
        oldpass = request.POST['oldpassword']
        newpass = request.POST['newpassword']
        confpass = request.POST['password_confirm']

        username = request.user.username
        
        user = authenticate(request, username=username, password=oldpass)
    
        if user:
            if newpass == confpass:
                u = User.objects.get(username=username)
                u.set_password(newpass)
                u.save()

                #Sending email after successful updation.

                # subject = 'Attetion! Your E-commerce Book Store account password has been changed'
                # message = f'Hi {user.username}, Your E-commerce Book Store account password has been changed'
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list = [user.email, ]
                # send_mail( subject, message, email_from, recipient_list )
                # print("Email Sent Succesfully!!")
                
                messages.info(request,"Password updated. Your session is logged out, Please login again")
                return redirect('/update_password')
            else:
                messages.info(request,"NewPassword & ConfirmedPassword not matching")
                return redirect('/update_password')
        
        else:
            messages.info(request,"OldPassword entered is incorrect")
            return redirect('/update_password')
        
         