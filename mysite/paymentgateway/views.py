from django.shortcuts import render, redirect
from myapp.models import Book
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def card(request):
    return render(request, "myapp/cards.html")

def payment_details(request):
    cardnum = request.POST.get('carddtl')
    num_list = list(cardnum)

    odd_sum = 0
    even_sum = 0
    dbl_evn_list = []

    for (idx, val) in enumerate(num_list):
        if (idx % 2) != 0:
            odd_sum += int(val)
        else:
            dbl_evn_list.append(int(val) * 2)

    dbl_list_str = ""

    for x in dbl_evn_list:
        dbl_list_str += str(x)

    dbl_list_str = list(dbl_list_str)
    for evn_list in dbl_list_str:
        even_sum += int(evn_list)

    net_sum = 0
    net_sum = odd_sum + even_sum
    if net_sum % 10 == 0:

        ids = list(request.session.get('cart').keys())
        books = Book.get_book_by_id(ids)
        bk = list(books)

        #Sending email after successful payment.

        # subject = 'Thank You for shopping with E-commerce Book Store | Order Details'
        # message = f'Hi {request.user.username}, Thank You for shopping with E-commerce Book Store \nPlease find your order details \n {bk}'
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [request.user.email, ]
        # send_mail( subject, message, email_from, recipient_list )
        # print("Email Sent Succesfully!!")
        
        
        return render(request, "myapp/confirm.html",{'books':books})
    else:
        messages.info(request,"Please enter valid Debit/Credit card")

    return render(request, "myapp/cards.html")