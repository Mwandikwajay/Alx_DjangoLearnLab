from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from .models import Post  # Import the Post model

# Home View
def home(request):
    return HttpResponse("Welcome to the Home Page!")

# Blog Posts View
def posts(request):
    return HttpResponse("This is the Blog Posts page.")

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created! You can now log in.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

# Profile View
@login_required
def profile(request):
    if request.method == 'POST':
        # Get updated user info from the form
        username = request.POST.get('username')
        email = request.POST.get('email')

        # Update the user object
        request.user.username = username
        request.user.email = email
        request.user.save()

        messages.success(request, "Your profile has been updated successfully!")
        return redirect('profile')

    return render(request, 'blog/profile.html')


# ---- CRUD Operations for Blog Posts ---- #

# ListView: Display all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Template for the post list
    context_object_name = 'posts'
    ordering = ['-published_date']  # Show newest posts first

# DetailView: Show a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # Template for a single post

# CreateView: Allow users to create a post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']  # Fields for the form
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the logged-in user as author
        return super().form_valid(form)

# UpdateView: Allow authors to edit their post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only the author can edit the post

# DeleteView: Allow authors to delete their post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')  # Redirect to post list after deletion
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only the author can delete the post
