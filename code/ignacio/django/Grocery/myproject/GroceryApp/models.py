# from xml.parsers.expat import model
from django.db import models

# Create your models here.

class GroceryItem(models.Model):
    item_name = models.CharField(max_length=200)
    date_created = models.DateField(null=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item_name