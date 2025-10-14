from django.urls import path

from orders import views as order_views

app_name = 'orders'

urlpatterns = [
    path('create-order/', order_views.create_order, name='create_order'),
]