from django.contrib import admin
from .models import *
from .models import Product


class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount', 'priceDis', 'category', 'created', 'updated')
    list_filter = ('price',)
    search_fields = ('name', 'id')
    inlines = [ProductImageInLine]

    # class Meta:
    #     model = Product


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    # list_display = ('name', 'price', 'discount', 'priceDis', 'text',)
    list_display = [field.name for field in ProductImage._meta.fields]


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]

    class Meta:
        model = ProductCategory
