from myblog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
# List brings multiple records to list out, CreateView creates a view, Detail will bring a single


class Main(ListView):
    model = Post
    template_name = 'main.html'


class Detail(DetailView):
    model = Post
    template_name = 'detail.html'


class CreatePost(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = '__all__'
