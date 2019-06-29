from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.view, name='orders'),
    path('orders-cart/<int:id>/', views.viewCart, name='orderCart'),
    path('del/<int:id>/', views.delO, name='del'),

]
