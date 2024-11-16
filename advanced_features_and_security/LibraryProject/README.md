
# Django Permissions and Groups Setup

## Overview
This project uses Django’s built-in **permissions** and **groups** system to control access to specific actions in the `bookshelf` app. Permissions define user access to actions like creating, editing, or deleting books, while groups help manage multiple permissions collectively.

## Default Permissions
Django provides default permissions for models like `Book`, such as:
- `add_book`
- `change_book`
- `delete_book`
- `view_book`

These permissions are automatically created after running migrations.

## Custom Permissions
To create custom permissions, add them in the `Meta` class of the model:

```python
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ('can_view', 'Can view book'),
            ('can_edit', 'Can edit book'),
            ('can_delete', 'Can delete book'),
        ]
```

## Creating and Assigning Groups
1. Go to the **Groups** section in the Django Admin panel (`/admin`).
2. Create groups such as `Reader`, `Librarian`, etc.
3. Assign appropriate permissions to each group.
4. Assign users to the groups.

## Using Permissions in Views
To restrict access to views based on permissions, use the `permission_required` decorator:

```python
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
```

## Example Views:
- **Create Book**: `@permission_required('bookshelf.can_create')`
- **Edit Book**: `@permission_required('bookshelf.can_edit')`
- **Delete Book**: `@permission_required('bookshelf.can_delete')`

## Customizing Permissions
You can create custom permission checks:

```python
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    
    if not request.user.has_perm('bookshelf.can_edit') or book.author != request.user:
        return HttpResponseForbidden("You do not have permission to edit this book.")
    
    # Continue with editing the book
```

## Testing Permissions
To assign permissions via Django shell:

```bash
$ python3 manage.py shell
```

```python
from django.contrib.auth.models import User, Group

user = User.objects.create_user('reader', 'reader@example.com', 'password')
group = Group.objects.get(name='Reader')
user.groups.add(group)
user.save()
```

## Conclusion
Permissions and groups provide a flexible way to control user access in Django. Custom permissions and group-based assignments offer fine-grained control over actions within the `bookshelf` app.
