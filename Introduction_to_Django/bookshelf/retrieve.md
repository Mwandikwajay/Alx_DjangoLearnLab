# Retrieve Operation
**Import the Model:**
```python
from bookshelf.models import Book
**Command:**
```python
retrieved_book = Book.objects.get(id=book.id)
retrieved_book
```

**Expected Output:**
```python
<Book: 1984 by George Orwell (1949)>
```