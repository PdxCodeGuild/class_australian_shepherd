from django.db import models
from datetime import datetime

class Todo_list(models.Model):
    title = models.CharField(max_length=100)
    objective = models.TextField(max_length=400)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField(default=datetime.now)
    in_progress = models.BooleanField()

    def __str__(self):
        return self.title