from django.urls import path, re_path
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # path('product/', views.product, name='product'),
    path('carts/<int:id>/', views.remove, name='remove'),
    path('carts/<slug:slug>/', views.update_to_cart, name='update_to_cart'),
    path('carts/', views.view, name='cart')

]
