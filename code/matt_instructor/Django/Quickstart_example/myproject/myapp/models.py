from django.db import models
from django.utils import timezone

class MyModel(models.Model):
    myfield = models.CharField(max_length=200)
    author = models.CharField(max_length=150, default='n/a')
    pub_date = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.myfield + ' by: ' + self.author 
