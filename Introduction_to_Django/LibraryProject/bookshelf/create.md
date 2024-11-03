# Create Operation
**Import the Model:**
```python
from bookshelf.models import Book
**Command:**
```python
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
<Book: 1984 by George Orwell (1949)>
