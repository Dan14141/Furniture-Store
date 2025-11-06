from django.urls import path
from main import views as main_views

app_name = 'main'
urlpatterns = [
    path('',main_views.IndexView.as_view(),name='index'),
    path('about/',main_views.AboutView.as_view(),name='about'),


]