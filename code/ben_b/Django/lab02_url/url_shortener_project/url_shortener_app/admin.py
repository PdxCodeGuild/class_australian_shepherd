from django.contrib import admin
from .models import UrlLink, UrlMeta

admin.site.register([UrlLink, UrlMeta])
