from django.db import models
from django.utils import timezone

class MyModel(models.Model):
    myfield = models.CharField(max_length=200)
    mytime = models.DateTimeField(default=timezone.now(), null=True)
    myboolean = models.BooleanField()
    
    def __str__(self):
        return self.myfield + " - " + self.myboolean