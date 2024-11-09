from django.urls import path
from . import views  # Import views here
from .views import list_books  # Explicitly import list_books

urlpatterns = [
    # Existing URL patterns
    path('list_books/', list_books, name='list_books'),  # Use list_books view here
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library details
    
    # New authentication URL patterns
    path('login/', views.user_login, name='login'),  # Login view
    path('logout/', views.user_logout, name='logout'),  # Logout view
    path('register/', views.register, name='register'),  # Register view
]
