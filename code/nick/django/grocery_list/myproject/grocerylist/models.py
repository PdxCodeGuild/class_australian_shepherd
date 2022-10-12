from django.db import models
from datetime import date

# Create your models here.


class ToDoList(models.Model):
    grocery_genre = models.CharField(max_length=20)
    item_description = models.CharField(max_length=255)
    created_date = models.DateField (default=date.today)
    completeBy_date = models.DateField(default=date.today)
    task_complete = models.BooleanField(default=False)
    date_complete = models.DateField(null=True)

    def __str__(self):
        return self.item_description