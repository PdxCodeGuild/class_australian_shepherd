from django.db import models

# Create your models here.
class Shorten(models.Model):
  long_url = models.TextField(max_length=2048)
  short_url = models.CharField(max_length=6)

  def __str__(self):
    return self.short_url
    # this is for rendering admin list view
