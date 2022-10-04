from unittest.util import _MAX_LENGTH
from django.db import models

class Url(models.Model):
    url = models.CharField(max_length=200)
    short = models.CharField(max_length=20)

    def __str__(self):
        return self.url