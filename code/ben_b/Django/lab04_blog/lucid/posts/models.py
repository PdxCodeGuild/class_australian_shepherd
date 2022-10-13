from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.body}'

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('posts:home', args=(self.pk,))
    
