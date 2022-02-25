from unicodedata import name
from django import template

register = template.Library()

@register.filter(name='cart_quantity')
def cart_quantity(books, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == books.id:
            return cart.get(id)
    return 0;

@register.filter(name='book_total')
def book_total(books, cart):
    return books.Price * cart_quantity(books, cart)

@register.filter(name="total_cart_price")
def total_cart_price(books, cart):
    sum = 0
    for b in books:
        sum += book_total(b , cart)

    return sum