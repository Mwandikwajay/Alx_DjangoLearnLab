from django.urls import path
from . import views

urlpatterns = [
    path('list_books/', views.list_books, name='list_books'),  # Keep the FBV for listing books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Add the CBV for library details
]
