from django.urls import path, re_path
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # path('product/', views.product, name='product'),
    path('products/search/', views.search, name='search'),

    path('products/', views.products, name='products'),
    path('products/<slug:slug_text>/', views.product, name='product'),
    path('<slug:slug_text_cat>/', views.products, name='productss'),


    path('', views.index, name='index'),

]
