from django.db import models

# Create your models here.
class GroceryModel(models.Model):
  GroceryItem = models.CharField(max_length=200)

  def __str__(self):
    return self.GroceryItem
