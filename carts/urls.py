from django.urls import path
from carts import views as carts_views

app_name = 'carts'
urlpatterns = [
    path('cart_add/',carts_views.CartAddView.as_view(),name='cart_add'),
    path('cart_change/',carts_views.CartChangeView.as_view(),name='cart_change'),
    path('cart_remove/',carts_views.CartRemoveView.as_view(),name='cart_remove'),
]