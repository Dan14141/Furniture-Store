from django.urls import path
from goods import views as goods_views

app_name = 'goods'
urlpatterns = [
    path('<slug:category_slug>/',goods_views.catalog,name='index'),
    path('<slug:category_slug>/<int:page>/',goods_views.catalog,name='index'),
    path('product/<slug:product_slug>/',goods_views.product,name='product'),
]