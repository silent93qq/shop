from django.db import models
from shop.models import Product


class Cart(models.Model):
    order_id = models.CharField(max_length=100,default=0)
    total = models.DecimalField(max_digits=100, decimal_places=0, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "Cart id: %s" % (self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, )
    line_total = models.DecimalField(default=10, max_digits=100, decimal_places=0)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        try:
            return str(self.cart.id)
        except:
            return self.product.name