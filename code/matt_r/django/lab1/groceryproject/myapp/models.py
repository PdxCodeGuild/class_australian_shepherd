from email.policy import default
from django.db import models

# Create your models here.

class grocerys(models.Model):
    item = models.CharField(max_length=200)
    quanity = models.IntegerField(default=1)
    date_created = models.DateTimeField()
    completed = models.BooleanField()

    def __str__(self):
        return self.item

