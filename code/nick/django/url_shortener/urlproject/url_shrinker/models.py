from email.policy import default
from django.db import models

# Create your models here.

class ConvexURL(models.Model):
    longURL = models.URLField(max_length=200)
    short_url = models.URLField(max_length=200)
    http_referral = models.TextField(max_length=220, null=True)

    def __str__(self):
        return self.short_url