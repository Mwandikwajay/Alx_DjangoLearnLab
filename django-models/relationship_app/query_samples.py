from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    # Query all books by a specific author
    books = Book.objects.filter(author__name=author_name)
    for book in books:
        print(f"Book Title: {book.title}, Author: {book.author.name}")

def list_books_in_library(library_name):
    # List all books in a library
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # ManyToMany relationship
    for book in books:
        print(f"Book Title: {book.title}, Library: {library.name}")

def retrieve_librarian_for_library(library_name):
    # Retrieve the librarian for a library
    library = Library.objects.get(name=library_name)
    librarian = library.librarian  # OneToOne relationship
    print(f"Librarian for {library.name}: {librarian.name}")

# Example usage
if __name__ == "__main__":
    # Replace these with actual library and author names from your database
    query_books_by_author('Author Name')  # Replace 'Author Name' with actual author's name
    list_books_in_library('Library Name')  # Replace 'Library Name' with actual library's name
    retrieve_librarian_for_library('Library Name')  # Replace 'Library Name' with actual library's name
