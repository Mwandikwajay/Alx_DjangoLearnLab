from django.db import models
# Author model represents an author of books.
class Author(models.Model):
    # Name of the author
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
# Book model represents a book written by an author.
class Book(models.Model):
     # Title of the book
    title = models.CharField(max_length=255)
     # Year the book was published
    publication_year = models.IntegerField()
     # Relationship with the Author model (one author can have many books)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
