from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# on_delete will delete all posts if we delete user


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + ', ' + str(self.author)
    # to send form for create post

    def get_absolute_url(self):
        return reverse('detail', args=(str(self.id)))
