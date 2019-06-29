import time

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse
from django.shortcuts import redirect

def checkout(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    com = request.POST.get('description')
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse("cart"))

    new_order, created = Order.objects.get_or_create(cart=cart)
    if created:
        new_order.order_id = cart.order_id
        new_order.costumer_name = name
        new_order.costumer_phone = phone
        new_order.comments = com
        new_order.save()

    if new_order.status == "finished":
        return HttpResponseRedirect(reverse('cart'))

    request.session.modified = True

    del request.session['cart_id']
    del request.session['items_total']

    return render(request, 'index.html')


def view(request):
    orders = Order.objects.all()

    return render(request, 'orders/orders.html', locals())


def viewCart(request, id):
    cart = Cart.objects.get(id=id)

    return render(request, 'orders/order_cart.html', locals())


def delO(request, id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    return HttpResponseRedirect(reverse('orders'))
