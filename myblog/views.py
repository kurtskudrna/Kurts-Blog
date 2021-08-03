from myblog.models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
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


class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('main')
