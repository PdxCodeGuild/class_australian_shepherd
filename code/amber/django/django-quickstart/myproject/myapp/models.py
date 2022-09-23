from django.db import models
from django.utils import timezone

# Create your models here.
class MyModel(models.Model):
    myfield = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    body = models.CharField(max_length=2000)
    timestamp = models.DateTimeField(default=timezone.now)
