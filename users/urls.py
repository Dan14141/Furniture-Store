from django.urls import path
from users import views as users_views

app_name = 'users'
urlpatterns = [
    path('login/',users_views.login,name='login'),
    path('registration/',users_views.registration,name='registration'),
    path('profile/',users_views.profile,name='profile'),
    path('logout/',users_views.logout,name='logout'),
    path('users-cart/', users_views.users_cart, name='users_cart'),


]