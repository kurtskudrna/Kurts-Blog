from myblog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# List brings multiple records to list out, Detail will bring a single


class Main(ListView):
    model = Post
    template_name = 'main.html'


class Detail(DetailView):
    model = Post
    template_name = 'detail.html'
