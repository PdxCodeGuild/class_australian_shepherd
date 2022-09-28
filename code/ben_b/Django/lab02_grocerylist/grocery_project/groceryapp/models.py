from django.db import models

class GroceryList(models.Model):
    grocery_item = models.CharField(max_length=200)
    
    def __str__(self):
        return self.grocery_item