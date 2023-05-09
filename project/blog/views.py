from django.shortcuts import render, get_list_or_404
from .models import Blog, Category
# Create your views here.

def home(request):
    Bolg_object = Blog.objects.filter(post_status='publish')
    context = {'BlogOject': Bolg_object}
    name = 'index.html'
    return render (request, name, context)

def category_deails(request, category_slug):
    category_url = get_list_or_404(Category, slug = category_slug)
    posts = Blog.objects.filter(category = category_url)
    name = 'category.html'
    context = {'posts':posts}
    return render (request, name, context)
