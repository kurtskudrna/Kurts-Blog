from django.urls import path
from django.views.generic import edit
from .views import CreateCat, CreateComment, EditPost, Main, Detail, CreatePost, DeletePost, Category

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('post/<int:pk>', Detail.as_view(), name='detail'),
    path('create_post', CreatePost.as_view(), name='create_post'),
    path('create_category', CreateCat.as_view(), name='create_cat'),
    path('edit/<int:pk>', EditPost.as_view(), name='edit_post'),
    path('delete/<int:pk>', DeletePost.as_view(), name='delete_post'),
    path('category/<str:category>/', Category, name='category'),
    path('create_comment/<int:pk>', CreateComment.as_view(), name='create_comment')
]
