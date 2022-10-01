from django.db import models
from django.utils import timezone

# Create your models here.


class GroceryItem(models.Model):
    item_name = models.CharField(max_length=200)
    requestor = models.CharField(max_length=200, null=True)
    item_description = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(default=timezone.now(), null=True)
    completed = models.BooleanField()
    # updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name
