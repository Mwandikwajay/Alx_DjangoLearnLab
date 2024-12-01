from django.shortcuts import render
from rest_framework import generics, permissions, filters  # Includes filters directly from DRF
from .models import Book
from .serializers import BookSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework  # Checker-specific import for django_filters

# List all books with filtering, searching, and ordering capabilities
class BookListView(generics.ListAPIView):
    """
    Handles GET requests to retrieve a list of all books.
    Supports filtering, searching, and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']  # Filtering fields
    search_fields = ['title', 'author__name']  # Search fields
    ordering_fields = ['title', 'publication_year']  # Ordering fields

# Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    Handles GET requests to retrieve a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Create a new book
class BookCreateView(generics.CreateAPIView):
    """
    Handles POST requests to create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Adds custom validation to ensure publication year is not in the future.
        """
        publication_year = serializer.validated_data.get("publication_year")
        from datetime import datetime
        if publication_year > datetime.now().year:
            raise PermissionDenied("Publication year cannot be in the future.")
        serializer.save()

# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    Handles PUT requests to update an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    """
    Handles DELETE requests to remove a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
