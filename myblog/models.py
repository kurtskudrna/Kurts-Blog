from django.db import models
from datetime import datetime, date
from django.urls import reverse
from django.contrib.auth.models import User

# on_delete will delete all posts if we delete user


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, default='sports')
    body = models.TextField()

    def __str__(self):
        return self.title + ', ' + str(self.author)
    # to send form for create post

    def get_absolute_url(self):
        return reverse('main')


class Category(models.Model):
    catname = models.CharField(max_length=255)

    def __str__(self):
        return self.catname
    # to send form for create post

    def get_absolute_url(self):
        return reverse('main')


class BlogComments(models.Model):
    post = models.ForeignKey(
        Post, related_name='comment_post', on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.user)
