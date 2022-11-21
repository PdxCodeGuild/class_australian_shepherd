from django.db import models
from django.urls import reverse

from users.models import CustomUser

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(CustomUser, related_name='posts', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title} - {self.created}'

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('posts:home', args=(self.pk,))
