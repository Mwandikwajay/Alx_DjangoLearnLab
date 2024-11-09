from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book  # Import Book model
from .models import Library  # Import Library model separately

# Existing function-based view (FBV) to list all books
def list_books(request):
    # Query all books from the database
    books = Book.objects.all()

    # Render the books using a template
    return render(request, 'relationship_app/list_books.html', {'books': books})

# New class-based view (CBV) for displaying library details and associated books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Define the template for rendering
    context_object_name = 'library'  # The context variable to use in the template
    
    def get_context_data(self, **kwargs):
        # Get the context data from the superclass (DetailView)
        context = super().get_context_data(**kwargs)
        
        # Add the list of books associated with this library to the context
        context['books'] = self.object.books.all()  # This is the Many-to-Many relationship with books
        return context
