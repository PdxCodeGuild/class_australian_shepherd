from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=69)
    body = models.TextField(max_length=666)
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.title} - {self.created}'

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('posts:home', args=(self.pk,))
