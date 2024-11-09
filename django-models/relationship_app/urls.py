from django.urls import path
from . import views  # Import views here
from django.contrib.auth.views import LoginView, LogoutView  # Import Django's built-in LoginView and LogoutView

urlpatterns = [
    # Existing URL patterns
    path('list_books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication views using CBVs
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]
