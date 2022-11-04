from django.db import models
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    user = models.ForeignKey('auth.User', related_name='blogposts', on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)
    date_edited = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.title} - {self.date_created}'
    
    class Meta:
        ordering = ['-date_created']
        
    def get_absolute_url(self):
        return reverse('gravy_app:home', args=(self.pk,))