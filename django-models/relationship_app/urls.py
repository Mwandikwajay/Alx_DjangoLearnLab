from django.urls import path
from . import views  # Import views here
from django.contrib.auth.views import LoginView, LogoutView  # Import Django's built-in LoginView and LogoutView

urlpatterns = [
    # Existing URL patterns
    path('list_books/', views.list_books, name='list_books'),  # Use list_books view here
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library details
    
    # New authentication URL patterns using CBVs
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Use LoginView CBV
    path('logout/', LogoutView.as_view(), name='logout'),  # Use LogoutView CBV
    path('register/', views.register, name='register'),  # Register view as function-based view (FBV)
]
