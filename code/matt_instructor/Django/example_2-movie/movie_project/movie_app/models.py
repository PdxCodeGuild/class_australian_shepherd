from pyexpat import model
from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=208)
    director = models.CharField(max_length=200)
    release_date = models.DateTimeField()
    in_theatres = models.BooleanField()
    genre = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name 
        