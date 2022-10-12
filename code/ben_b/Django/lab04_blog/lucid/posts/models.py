from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.body}'

    # class Meta:
    #     ordering = ['-created']

    def get_absolute_url(self):
        return reverse('posts:home', args=(self.pk,))
    
