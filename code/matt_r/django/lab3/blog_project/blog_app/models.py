from django.db import models
from django.urls import reverse

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']


    def get_absolute_url(self):
        return reverse('blog_app:home', args=(self.pk,))