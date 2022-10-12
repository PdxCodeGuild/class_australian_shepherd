from turtle import title
from django.db import models
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    user = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    is_public = models.BooleanField(null=True)
    date_created = models.DateField(auto_now_add=True)
    date_edited = models.DateField(auto_now=True)
    
