from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated  # Import permissions
from .models import Book
from .serializers import BookSerializer

# List API View
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ViewSet with Authentication Permissions
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Enforce authentication
