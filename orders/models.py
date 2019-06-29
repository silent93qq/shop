from django.db import models
from shop.models import Product
from cart.models import Cart

STATUS_CHOICE = (
    ('Обзвон', 'Обзвон'),
    ("пох", "пох"),
    ("finished","finished")

)


class Order(models.Model):
    order_id = models.CharField(max_length=120, default='abc', unique=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,blank=True, default=None, )
    costumer_name = models.CharField(verbose_name="Название", max_length=20, default='')
    costumer_phone = models.CharField(verbose_name='Номер тел.', null=True, max_length=20, )
    comments = models.TextField(verbose_name='Пожелание', null=True)
    status = models.CharField(max_length=120, choices=STATUS_CHOICE, default="Обзвон")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "Заказ",
        verbose_name_plural = "Заказы"


