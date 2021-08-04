from django.contrib import admin
from .models import BlogComments, Category, Post
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(BlogComments)
