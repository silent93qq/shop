from datetime import datetime
import time
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .models import Cart, CartItem

from shop.models import Product
from orders.utils import id_generator


def view(request):
    date = datetime.now()

    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    print(the_id)
    if the_id:
        cart = Cart.objects.get(id=the_id)
        ord_id = cart.order_id

        new_total = 0
        for item in cart.cartitem_set.all():
            line_total = int(item.product.price) * item.quantity
            new_total += line_total
        request.session['items_total'] = cart.cartitem_set.count()
        cart.total = new_total
        cart.save()

        context = {"cart": cart, 'date': date, "ord_id": ord_id}
    else:
        empty_mes = "you cart empty"
        context = {"empty": True, "empty_mes": empty_mes, 'date': date}

    return render(request, 'cart/cart.html', context)


def remove(request, id):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse('cart'))

    cartitem = CartItem.objects.get(id=id)
    cartitem.delete()
    return HttpResponseRedirect(reverse('cart'))


def update_to_cart(request, slug, ):
    request.session.set_expiry(120000)
    try:
        qty = request.GET.get('qty')
        update_qty = True
    except:
        qty = None
        update_qty = False

    try:
        attr = request.GET.get('attr')
    except:
        attr = None

    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.order_id = id_generator()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get_or_create(id=the_id)

    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass

    cart_item, created = CartItem.objects.get_or_create(cart_id=the_id, product=product)

    if created:
        print("eea")
    if update_qty and qty:
        if int(qty) == 0:
            cart_item.delete()
        else:
            cart_item.quantity = qty
            cart_item.save()
    else:
        pass


    return HttpResponseRedirect(reverse('cart'))
