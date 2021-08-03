from django.urls import path
from django.views.generic import edit
from .views import EditPost, Main, Detail, CreatePost

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('post/<int:pk>', Detail.as_view(), name='detail'),
    path('create_post', CreatePost.as_view(), name='create_post'),
    path('edit/<int:pk>', EditPost.as_view(), name='edit_post')
]
