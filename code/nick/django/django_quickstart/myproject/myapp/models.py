from django.db import models
from django.utils import timezone

# Create your models here.
class MyModel(models.Model):
    author = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=timezone.now, null=True)
    
    def __str__(self):
        return self.author
