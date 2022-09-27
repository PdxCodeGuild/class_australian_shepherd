from django.db import models
from django.utils import timezone

# Create your models here.
class GroceryModel(models.Model):
  GroceryItem = models.CharField(max_length=200)
  DateAdded = models.DateTimeField(default=timezone.now)
  ToDo = models.BooleanField(null=True)

  def __str__(self):
    return self.GroceryItem
