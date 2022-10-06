from django.db import models

class UrlMeta(models.Model):
    name = models.CharField(max_length=200, null=True)
    content_length = models.CharField(max_length=200, null=True)
    csrf_cookie = models.CharField(max_length=200, null=True)
    

    def __str__(self):
        return self.name

class UrlLink(models.Model):
    name = models.CharField(max_length=200)
    url_long = models.URLField(max_length=200)
    url_short = models.CharField(max_length=200, null=True)
    url_meta = models.ForeignKey(UrlMeta, on_delete=models.CASCADE, related_name='UrlLinks')

    def __str__(self):
        return self.name
