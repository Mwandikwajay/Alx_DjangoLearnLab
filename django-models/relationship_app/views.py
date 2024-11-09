from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic.detail import DetailView  # Correct import for DetailView
from .models import Book  # Import Book model
from .models import Library  # Import Library model separately

# Existing function-based view (FBV) to list all books
def list_books(request):
    # Query all books from the database
    books = Book.objects.all()

    # Render the books using a template
    return render(request, 'relationship_app/list_books.html', {'books': books})

# New class-based view (CBV) for displaying library details and associated books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Define the template for rendering
    context_object_name = 'library'  # The context variable to use in the template
    
    def get_context_data(self, **kwargs):
        # Get the context data from the superclass (DetailView)
        context = super().get_context_data(**kwargs)
        
        # Add the list of books associated with this library to the context
        context['books'] = self.object.books.all()  # This is the Many-to-Many relationship with books
        return context

# Register View for user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login View for user login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page or another page after login
        else:
            return render(request, 'relationship_app/login.html', {'error': 'Invalid credentials'})
    return render(request, 'relationship_app/login.html')

# Logout View for user logout
@login_required
def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')
