from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from relationship_app.models import Book, Library

# Existing function-based view (FBV) to list all books
def list_books(request):
    # Query all books from the database
    books = Book.objects.all()

    # Create a response with a simple text list of books and authors
    response_content = "List of Books and Authors:\n\n"
    
    for book in books:
        response_content += f"Book Title: {book.title}, Author: {book.author.name}\n"
    
    # Return the response as a plain text response
    return HttpResponse(response_content, content_type='text/plain')

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
