from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    """handles traffic from homepage"""
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    """handles logic for about page"""
    return render(request, 'blog/about.html', {'title': 'About'})
