import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jo.settings')
django.setup()

from faker import Faker
from shop.models import Product, ProductImage, ProductCategory
from django.utils import timezone


def createFaker(N):
    fake = Faker()
    for _ in range(N):
        ProductCategory.objects.create(
            name="name",
            is_active=True,
            slug="name",
        )

        pro = Product.objects.create(
            name=fake.name(),
            discount=0,
            price=123,
            priceDis=555,
            text=fake.name(),
            is_active=1,
            created=timezone.now(),
            updated=timezone.now(),
            category_id=1,
        )

        ProductImage.objects.create(
            product_id=pro.id,
            image='media/8_DW8py9z.png',
            is_main=True,
            is_active=True,
        )


createFaker(10)
