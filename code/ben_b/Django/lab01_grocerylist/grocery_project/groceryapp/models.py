from django.db import models


class GroceryList(models.Model):
    completed = models.BooleanField()
    grocery_item = models.CharField(max_length=200)
    date = models.DateTimeField()
    
    def __str__(self):
        return self.grocery_item