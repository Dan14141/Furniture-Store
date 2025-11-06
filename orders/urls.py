from django.urls import path

from orders import views as order_views

app_name = 'orders'

urlpatterns = [
    path('create-order/', order_views.CreateOrderView.as_view(), name='create_order'),
]