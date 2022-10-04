from django.db import models
from datetime import datetime


class Todo_list(models.Model):
    title = models.CharField(max_length=100)
    objective = models.TextField(max_length=400)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField(default=datetime.now)
    in_progress = models.BooleanField()
    priority = models.CharField(max_length=100, default="Low")

    def __str__(self):
        return self.title


class Notes(models.Model):
    note = models.TextField(max_length=1000)

    def __str__(self):
        return self.note
