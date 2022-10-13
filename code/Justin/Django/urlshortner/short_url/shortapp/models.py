from django.db import models


# Create your models here.


class ShortenedURL(models.Model):
    short_url = models.CharField(max_length=200)
    long_url = models.URLField(max_length=200)

    def __str__(self):
        return self.short_url
