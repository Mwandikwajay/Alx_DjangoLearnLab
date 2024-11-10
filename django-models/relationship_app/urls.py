from django.urls import path
from .views import list_books  # Explicitly import list_books

urlpatterns = [
    # Existing URL patterns
    path('list_books/', list_books, name='list_books'),  # Correct import of list_books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication views
    path('login/', views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    # Custom Permissions urls
    path("books/add_book/", views.add_book, name="add_book"),
    path("books/edit_book/<int:book_id>/", views.edit_book, name="edit_book"),
    path("books/delete_book/<int:book_id>/", views.delete_book, name="delete_book"),
]