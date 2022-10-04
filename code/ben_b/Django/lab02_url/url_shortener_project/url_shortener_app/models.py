from django.db import models

class urlLink(models.Model):
    name = models.CharField(max_length=200)
    url_long = models.URLField(max_length=200)
    url_short = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name