from myblog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogComments, Category, Post
from django.urls import reverse_lazy
from .forms import CommentForm, CreateForm, EditForm
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
    cat_posts = Post.objects.filter(category=category.replace('-', ' '))
    return render(request, 'category.html', {'category': category.replace('-', ' '), 'cat_posts': cat_posts})


class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('main')


class CreateComment(CreateView):
    model = BlogComments
    form_class = CommentForm
    template_name = 'new_comment.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
