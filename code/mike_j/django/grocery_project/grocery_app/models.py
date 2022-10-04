from django.db import models

class GroceryItem(models.Model):
    item = models.CharField(max_length=200)
    timestamp = models.DateTimeField(null=True)
    complete = models.BooleanField()
    
    def __str__(self):
        return self.item