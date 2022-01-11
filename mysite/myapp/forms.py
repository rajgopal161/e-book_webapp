from django import forms
from django.forms import fields, models
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['Name', 'Desc', 'Price', 'image']