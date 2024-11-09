from django.shortcuts import render
from .models import Book  # Import your Book model

# Function-based view to display all books
def list_books(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})


    
from django.shortcuts import render
from django.views.generic import DetailView
from relationship_app.models import Library

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Make sure the template is correctly referenced
    context_object_name = 'library'