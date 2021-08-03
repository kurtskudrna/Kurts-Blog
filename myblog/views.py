from myblog.models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import CreateForm
# List brings multiple records to list out, CreateView creates a view, Detail will bring a single


class Main(ListView):
    model = Post
    template_name = 'main.html'


class Detail(DetailView):
    model = Post
    template_name = 'detail.html'


class CreatePost(CreateView):
    model = Post
    form_class = CreateForm
    template_name = 'create_post.html'


class EditPost(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = '__all__'
