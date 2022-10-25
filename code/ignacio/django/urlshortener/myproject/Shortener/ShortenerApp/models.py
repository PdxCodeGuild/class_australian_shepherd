from django.db import models

# Create your models here.

class shrink(models.Model):
    url = models.CharField(max_length=200)
    short_url = models.URLField(max_length=100)
    def __str__(self):
        return self.url