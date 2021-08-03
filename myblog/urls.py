from django.urls import path
from .views import Main, Detail, CreatePost

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('post/<int:pk>', Detail.as_view(), name='detail'),
    path('create_post', CreatePost.as_view(), name='create_post')
]
