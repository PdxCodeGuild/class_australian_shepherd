from django.db import models

class MyModel(models.Model):
    myfield = models.CharField(max_length=200)
    mytext = models.CharField(max_length=200, null=True, blank=True)
    mytime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.myfield + ' - ' + self.mytext