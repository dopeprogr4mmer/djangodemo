from django.http import Http404
from django.shortcuts import render
from .models import Blog

def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})

def blog_detail(request,pk):

    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        raise Http404('Blog Does not exist')
    return render(request, 'detail.html', {'blog':blog})