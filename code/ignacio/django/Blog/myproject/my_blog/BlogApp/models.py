from django.db import models,
from django.contrib.auth.models import User
from django.urls import reverse

class blog_post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length = 250)
    user = models.ForeignKey(User)
    public = models.BooleanField(default = False)
    date_created = models.DateTimeField(auto_now=True)
    date_edited = (models.DateTimeField(auto_now=True))

    
    def __str__(self):
        return f'{self.title} - {self.date_created}'

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('posts:home', args=(self.pk,))