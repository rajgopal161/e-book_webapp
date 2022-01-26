from django.shortcuts import redirect, render, resolve_url
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to my web page!!!</h1> <a href=" 'products' "> Click Here <br> </a>")

def products(request):
    book_list = Book.objects.all()
    context = {
        'book_list': book_list
    }
    return render(request,'myapp/products.html', context)

def product_detail(request, book_name):
    book = Book.objects.get(Name=book_name)
    context = {
        'book' : book
    }
    return render(request,'myapp/productdetails.html', context)

def add_book(request):
    if request.method == 'POST':
        Name = request.POST.get('Name',)
        Desc = request.POST.get('Desc',)
        Price = request.POST.get('Price',)
        image = request.FILES['image']

        book = Book(Name=Name, Desc=Desc, Price=Price, image=image)
        book.save()
        return redirect('/products/')

    return render(request,'myapp/add_book.html')


def book_update(request,book_name):
    book = Book.objects.get(Name=book_name)
    form = BookForm(request.POST or None, request.FILES, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/products/')

    return render(request, 'myapp/edit.html', {'form':form, 'book':book})

def delete_book(request, name):
    if request.method == 'POST':
        book = Book.objects.get(Name=name)
        book.delete()
        return redirect('/products/')
    return render(request,'myapp/delete.html')

#code not working for search

def product_search(request, book_name):
    book_list = Book.objects.all()
    
    context = {
        'book_list': book_list
    }
    if book_name in book_list == True:
        return render(request,'myapp/products.html', context)
    else:
        return HttpResponse("<h1>Book not found!!!</h1>")

    
    return render(request,'myapp/base.html', context)

#code not working for search

def search(request):        
    if request.method == 'GET': # this will be GET now      
        book_name =  request.GET.get('search') # do some research what it does       
        try:
            status = Book.objects.filter(bookname__icontains=book_name) # filter returns a list so you might consider skip except part
        except Book.DoesNotExist:
            status = None
        return render(request,'myapp/search.html',{"books":status})
    else:
        return render(request,'myapp/search.html',{})