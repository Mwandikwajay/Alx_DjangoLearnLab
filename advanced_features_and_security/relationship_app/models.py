from django.db import models
from django.conf import settings  # For AUTH_USER_MODEL

# Author Model
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book Model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    class Meta:
        permissions = [
            ('can_add_book', 'Can add a book'),
            ('can_change_book', 'Can edit a book'),
            ('can_delete_book', 'Can delete a book'),
        ]

    def __str__(self):
        return self.title


# Library Model
class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name


# Librarian Model
class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name


# UserProfile Model to hold role information for users
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    # Use AUTH_USER_MODEL to dynamically reference the custom user model
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"  # Adjust based on the CustomUser model fields
