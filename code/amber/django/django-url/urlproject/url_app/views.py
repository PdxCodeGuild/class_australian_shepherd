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

def random_url():
  length = 6
  short_code = ''.join(random.choices(string.printable), k=length)

  return short_code

def add_url(request):
  long_url = request.POST['long_url']
  short_url = random_url()
  shorten = Shorten(long_url=long_url, short_url=short_url)
  shorten.save()

  return redirect('url_app:add_url')
