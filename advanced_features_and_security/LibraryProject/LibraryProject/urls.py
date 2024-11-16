from django.contrib import admin
from django.urls import path, include
from relationship_app import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin
    path('', views.list_books, name='home'),  # Redirect root URL to list_books view
    path('list_books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    # Make sure the following line is as is
    path('books/', include('bookshelf.urls')),  # Correct URL inclusion for bookshelf app
]
