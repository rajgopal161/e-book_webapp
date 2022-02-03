from pyexpat import model
from django import forms
from django.forms import fields, models
from .models import Book
from account.models import UserAuth

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['Name', 'Desc', 'Price', 'image']

class UserAuthForm(forms.ModelForm):
    class Meta:
        model = UserAuth
        fields = ['username', 'email', 'password']  