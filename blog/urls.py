from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog-home'),
    path('order-checker/', views.order_checker, name='blog-order-checker'),
    path('payment/', views.payment, name='blog-payment'),
]
