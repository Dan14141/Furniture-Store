from django.urls import path
from goods import views as goods_views

app_name = 'goods'
urlpatterns = [
    path('',goods_views.catalog,name='index'),
    path('product/',goods_views.product,name='product'),
]