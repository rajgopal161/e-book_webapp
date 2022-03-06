from email import message
from urllib import request
from django.contrib import messages
from .models import Cart
from django.shortcuts import redirect, render
from myapp.models import Book

# Create your views here.
def add_cart(request, book_name):
    book = Book.objects.get(Name=book_name)
    
    product = request.POST.get('bookid')
    cart = request.session.get('cart')
    if cart:
        quantity = cart.get(product)
        if quantity:
            cart[product] = quantity + 1
        else:
            cart[product] = 1
    else:
        cart = {}
        cart[product] = 1
    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect('/products/' )

def cart(request):
    ids = list(request.session.get('cart').keys())
    books = Book.get_book_by_id(ids)
    
    return render(request, 'myapp/cart.html', {'books':books})


def remove_item(request):
    product = request.POST.get('bookid')
    cart = request.session.get('cart')
    if product in cart:
        cart.pop(product)
        print(cart)

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect('/cart/' )

def inc_dec(request):
    inc = request.POST.get('inc')
    dec = request.POST.get('dec')
    product = request.POST.get('bookid')
    cart = request.session.get('cart')
    if cart:
        quantity = cart.get(product)
        
        if quantity>0:
            print(quantity)
            if inc:
                cart[product] = quantity + 1
            elif dec:
                cart[product] = quantity - 1
    
    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect('/cart/' )