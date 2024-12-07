from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm

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
