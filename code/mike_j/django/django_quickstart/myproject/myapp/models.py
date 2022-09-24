from django.db import models

class MyModel(models.Model):
    myfield = models.CharField(max_length=200)
    mytextfield = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.myfield
