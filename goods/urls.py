from django.urls import path
from goods import views as goods_views

app_name = 'goods'
urlpatterns = [
    path('search/',goods_views.CatalogView.as_view(),name='search'),
    path('<slug:category_slug>/',goods_views.CatalogView.as_view(),name='index'),
    path('product/<slug:product_slug>/',goods_views.ProductView.as_view(),name='product'),

]