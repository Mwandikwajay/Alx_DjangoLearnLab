# Create Operation

**Command:**
```python
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

**Expected Output:**
```python
<Book: 1984 by George Orwell (1949)>
```


---

# Retrieve Operation

**Command:**
```python
retrieved_book = Book.objects.get(id=book.id)
retrieved_book
```

**Expected Output:**
```python
<Book: 1984 by George Orwell (1949)>
```


---

# Update Operation

**Command:**
```python
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
```

**Expected Output After Retrieval:**
```python
<Book: Nineteen Eighty-Four by George Orwell (1949)>
```


---

# Delete Operation

**Command:**
```python
retrieved_book.delete()
```

**Expected Output:**
```python
(1, {'bookshelf.Book': 1})
```

**Confirmation Command:**
```python
Book.objects.all()
```

**Expected Output:**
```python
<QuerySet []>
```