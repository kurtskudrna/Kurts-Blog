from myblog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post
from django.urls import reverse_lazy
from .forms import CreateForm, EditForm
# List brings multiple records to list out, CreateView creates a view, Detail will bring a single


class Main(ListView):
    model = Post
    template_name = 'main.html'
    # puts newest blog on top
    ordering = ['-date']


class Detail(DetailView):
    model = Post
    template_name = 'detail.html'


class CreatePost(CreateView):
    model = Post
    form_class = CreateForm
    template_name = 'create_post.html'


class CreateCat(CreateView):
    model = Category
    template_name = 'create_cat.html'
    fields = '__all__'


def Category(request, category):
    cat_posts = Post.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'cat_posts': cat_posts})


class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('main')
