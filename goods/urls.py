from django.urls import path
from goods import views as goods_views

app_name = 'goods'
urlpatterns = [
    path('search/',goods_views.catalog,name='search'),
    path('<slug:category_slug>/',goods_views.catalog,name='index'),
    path('product/<slug:product_slug>/',goods_views.product,name='product'),

]