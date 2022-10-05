from email.policy import default
from django.db import models

# Create your models here.
class Urlshortner(models.Model):
    long_url = models.URLField(max_length=200, default="https://www.google.com")
    short_code = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.long_url