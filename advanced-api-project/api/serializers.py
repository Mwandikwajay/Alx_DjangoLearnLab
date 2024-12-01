from rest_framework import serializers
from .models import Author, Book

# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Validate publication_year to ensure it is not in the future
    def validate_publication_year(self, value):
        from datetime import datetime
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
# Serializer for the Author model
# Includes a nested serializer for related books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested BookSerializer

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
