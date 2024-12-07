from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),

    # Blog Post Management
    path('posts/', PostListView.as_view(), name='post-list'),  # List all posts
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View single post
    path('posts/new/', PostCreateView.as_view(), name='post-create'),  # Create a post
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),  # Edit a post
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
