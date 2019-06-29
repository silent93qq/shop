from django.contrib import admin
from .models import *




@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # list_display = ('name', 'price', 'discount', 'priceDis', 'text',)
    list_display = [field.name for field in Order._meta.fields]



