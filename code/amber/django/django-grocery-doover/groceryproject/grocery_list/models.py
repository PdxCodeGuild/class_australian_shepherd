from django.db import models
from django.utils import timezone

# Create your models here.
class GroceryModel(models.Model):
  groceryitem = models.CharField(max_length=200)
  dateadded = models.DateTimeField(default=timezone.now)
  todo = models.BooleanField(null=True)

  def __str__(self):
    return self.groceryitem
