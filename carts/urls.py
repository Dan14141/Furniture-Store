from django.urls import path
from carts import views as carts_views

app_name = 'carts'
urlpatterns = [
    path('cart_add/',carts_views.cart_add,name='cart_add'),
    path('cart_change/',carts_views.cart_change,name='cart_change'),
    path('cart_remove/',carts_views.cart_remove,name='cart_remove'),
]