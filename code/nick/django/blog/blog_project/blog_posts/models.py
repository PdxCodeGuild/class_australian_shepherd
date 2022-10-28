from email.policy import default
from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('auth.User', related_name='blog_posts', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=2000)
    public = models.BooleanField(default=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.created}'

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('blog_posts:home')
