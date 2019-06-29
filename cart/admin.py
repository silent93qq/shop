from .models import *

from django.contrib import admin

from .models import Cart, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    class Meta:
        model = Cart


admin.site.register(CartItem)
