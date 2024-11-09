from django.shortcuts import render
from relationship_app.models import Book

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database

    
from django.shortcuts import render
from django.views.generic import DetailView
from relationship_app.models import Library

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Make sure the template is correctly referenced
    context_object_name = 'library'