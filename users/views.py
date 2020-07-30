from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    """handles user registration"""
    # checks if this is a POST request
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # checks if information is valid
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        # not a POST request; creates a blank form
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
