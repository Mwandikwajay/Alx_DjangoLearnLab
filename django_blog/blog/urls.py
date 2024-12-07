from django.urls import path
from django.contrib.auth import views as auth_views  # Import auth views
from . import views

urlpatterns = [
    path('', views.home, name='home'),         # Home Page
    path('posts/', views.posts, name='posts'), # Blog Posts Page
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'), # Register Page
    path('profile/', views.profile, name='profile'),
]
