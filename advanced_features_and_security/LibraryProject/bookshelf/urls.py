from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  # This is now mapped to '/books/' due to the inclusion in the project-level urls
    path('create/', views.create_book, name='create_book'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
]
