from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import ValidationError
from .models import Book
from .serializers import BookSerializer


# Retrieve a list of books
class BookListView(generics.ListAPIView):
    """
    Handles GET requests to retrieve a list of all books.
    Allows filtering by title, author, and publication_year,
    searching by book title and author's name,
    and ordering results by title or publication year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']  # Nested search for Author's name
    ordering_fields = ['title', 'publication_year']  # Allow ordering by these fields

# Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    Handles GET requests to retrieve a single book by its ID.
    Allows unauthenticated users to view the data.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Create a new book
class BookCreateView(generics.CreateAPIView):
    """
    Handles POST requests to create a new book.
    Only accessible to authenticated users.
    Custom validation prevents future publication years.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Adds custom validation to ensure the publication year is not in the future.
        """
        publication_year = serializer.validated_data.get("publication_year")
        from datetime import datetime
        if publication_year > datetime.now().year:
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()

# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    Handles PUT requests to update an existing book.
    Only accessible to authenticated users.
    Logs the update operation for debugging purposes.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        """
        Logs the book title being updated for debugging.
        """
        instance = self.get_object()
        print(f"Updating Book: {instance.title}")
        serializer.save()

# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    """
    Handles DELETE requests to remove a book.
    Only accessible to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
