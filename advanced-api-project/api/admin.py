from django.contrib import admin
from .models import Author, Book

# Register models for admin panel
admin.site.register(Author)
admin.site.register(Book)