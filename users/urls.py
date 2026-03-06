from django.urls import path
from users import views as users_views

app_name = 'users'
urlpatterns = [
    path('login/',users_views.UserLoginView.as_view(),name='login'),
    path('registration/',users_views.UserRegistrationView.as_view(),name='registration'),
    path('profile/',users_views.UserProfileView.as_view(),name='profile'),
    path('logout/',users_views.UserLogoutView.as_view(),name='logout'),
    path('users-cart/', users_views.UserCartView.as_view(), name='users_cart'),


]