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