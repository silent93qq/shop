from django.db import models
from django.db.models.signals import pre_save
from shop.utils import unique_slug_generator
from django.urls import reverse
from tinymce.models import HTMLField


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100, default='')
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


pre_save.connect(slug_generator, sender=ProductCategory)


class Product(models.Model):
    DISCOUNT_CHOICES = (
        (0, 'Нет'),
        (1, 'Да')
    )

    name = models.CharField(verbose_name="Название", max_length=100, default='')
    discount = models.IntegerField(verbose_name="Скидка", choices=DISCOUNT_CHOICES)
    price = models.IntegerField(verbose_name='Цена', null=True)
    priceDis = models.IntegerField(verbose_name="Новая Цена", null=True)
    is_active = models.BooleanField(default=True)
    text = HTMLField(verbose_name="Описание", max_length=100000, default='')

    slug = models.SlugField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE, )
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})


pre_save.connect(slug_generator, sender=Product)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, default=None, on_delete=models.CASCADE, )
    image = models.ImageField(verbose_name='Картинка', null=True, blank=True, upload_to="media/")
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"
        ordering = ['-created']
