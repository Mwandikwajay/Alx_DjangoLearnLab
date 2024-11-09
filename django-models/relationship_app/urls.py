from django.urls import path
from . import views  # Import views here
from django.contrib.auth.views import LoginView, LogoutView  # Import Django's built-in LoginView and LogoutView

from django.urls import path
from . import views  # Ensure views are imported correctly
from django.contrib.auth.views import LoginView, LogoutView  # Import Django's built-in LoginView and LogoutView

urlpatterns = [
    # Existing URL patterns
    path('list_books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication views using CBVs
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    # Secured views for adding, editing, and deleting books
    path('books/add/', views.add_book, name='add_book'),  # Secured add book view
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),  # Secured edit book view
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),  # Secured delete book view
]
