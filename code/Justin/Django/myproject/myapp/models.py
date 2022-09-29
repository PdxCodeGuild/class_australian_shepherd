from django.db import models
from django.utils import timezone

# Create your models here.


class MyModel(models.Model):
    myfield = models.CharField(max_length=200)
    myauthor = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(default=timezone.now(), null=True)
    # updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.myfield
