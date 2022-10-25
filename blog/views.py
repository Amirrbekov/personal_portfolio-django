from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def all_blogs_view(request):

    blogs = Blog.objects.order_by("-created_at")

    context = {}

    context['blogs']=blogs

    return render(request, 'blog.html', context)

def detail_view(request, id):
    blogs = get_object_or_404(Blog, id = id)
    context = {}
    context['blogs']=blogs

    return render(request, 'detail.html', context)
