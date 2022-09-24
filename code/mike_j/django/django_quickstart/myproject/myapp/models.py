from django.db import models
from django.utils import timezone

class MyModel(models.Model):
    myfield = models.CharField(max_length=200)
    mytextfield = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=200, null=True)
    timestamp = models.DateTimeField(default=timezone.now, null=True)
    
    def __str__(self):
        return self.myfield
