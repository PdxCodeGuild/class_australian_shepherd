from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

class createpost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length = 250)
    # user
    public = models.BooleanField(default = )
    
    def __str__(self):
        return self.myfield