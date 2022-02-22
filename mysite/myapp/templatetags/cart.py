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