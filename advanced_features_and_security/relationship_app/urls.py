from django.urls import path
from .views import list_books
from . import views

urlpatterns = [
    # Book-related views
    path('list_books/', list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication views
    path('login/', views.user_login, name='login'),  # Use user_login instead of LoginView
    path('logout/', views.user_logout, name='logout'),  # Use user_logout instead of LogoutView
    path('register/', views.register, name='register'),
    
    # Role-based views
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    # Book management views with permissions
    path("books/add_book/", views.add_book, name="add_book"),
    path("books/edit_book/<int:book_id>/", views.edit_book, name="edit_book"),
    path("books/delete_book/<int:book_id>/", views.delete_book, name="delete_book"),
]
