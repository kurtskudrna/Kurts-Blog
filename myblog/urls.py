from django.urls import path
from django.views.generic import edit
from .views import EditPost, Main, Detail, CreatePost, DeletePost

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('post/<int:pk>', Detail.as_view(), name='detail'),
    path('create_post', CreatePost.as_view(), name='create_post'),
    path('edit/<int:pk>', EditPost.as_view(), name='edit_post'),
    path('delete/<int:pk>', DeletePost.as_view(), name='delete_post'),
]
