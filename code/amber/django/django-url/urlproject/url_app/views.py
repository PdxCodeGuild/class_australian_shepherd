from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
import random
import string
from .models import Shorten

# Create your views here.
def home(request):
  all_urls = Shorten.objects.all()
  context = {
    'all_urls': all_urls
  }

  return render(request, 'url_app/home.html', context)
