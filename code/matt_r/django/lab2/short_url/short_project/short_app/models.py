from django.db import models

# Create your models here.

class Short(models.Model):
    website = models.URLField(max_length=200)
    short_url = models.CharField(max_length=50)

    def __str__(self):
        return self.website