from relationship_app.models import Author, Book, Library, Librarian
from django.core.exceptions import ObjectDoesNotExist

def query_books_by_author(author_name):
    # Query all books by a specific author
    try:
        # Get the Author object by name
        author = Author.objects.get(name=author_name)
        
        # Query all books by this author using the foreign key relationship
        books = Book.objects.filter(author=author)
        
        if books.exists():
            for book in books:
                print(f"Book Title: {book.title}, Author: {book.author.name}")
        else:
            print(f"No books found for author: {author_name}")
    except Author.DoesNotExist:
        print(f"No author found with the name: {author_name}")

def list_books_in_library(library_name):
    # List all books in a library
    try:
        # Get the Library object by name
        library = Library.objects.get(name=library_name)
        
        # Retrieve books associated with the library
        books = library.books.all()  # ManyToMany relationship
        
        if books.exists():
            for book in books:
                print(f"Book Title: {book.title}, Library: {library.name}")
        else:
            print(f"No books found in library: {library_name}")
    except Library.DoesNotExist:
        print(f"No library found with the name: {library_name}")

def retrieve_librarian_for_library(library_name):
    # Retrieve the librarian for a library
    try:
        # Get the Library object by name
        library = Library.objects.get(name=library_name)
        
        # Retrieve the librarian associated with the library
        librarian = library.librarian  # OneToOne relationship
        print(f"Librarian for {library.name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name: {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}")

# Example usage
if __name__ == "__main__":
    # Replace these with actual library and author names from your database
    query_books_by_author('J.K. Rowling')  # Replace with an actual author's name
    list_books_in_library('Central Library')  # Replace with an actual library's name
    retrieve_librarian_for_library('Central Library')  # Replace with an actual library's name
