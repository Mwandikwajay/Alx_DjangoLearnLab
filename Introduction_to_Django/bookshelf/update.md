# Update Operation
**Import the Model:**
```python
from bookshelf.models import Book
**Command:**
```python
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
```

**Expected Output After Retrieval:**
```python
<Book: Nineteen Eighty-Four by George Orwell (1949)>
```