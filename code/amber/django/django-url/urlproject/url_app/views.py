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
  short_code = ''.join(random.choices(string.ascii_letters, k=6))

  return short_code

def add_url(request):
  long_url = request.POST['long_url']
  short_url = random_url()
  shorten = Shorten(long_url=long_url, short_url=short_url)
  shorten.save()

  return redirect('url_app:home')

def sendview(request, id):
  url = get_object_or_404(Shorten, id=id)
  data = url.long_url

  return HttpResponseRedirect(data)

def delete_url(request, id):
  url_obj = get_object_or_404(Shorten, id=id)
  url_obj.delete()

  return redirect('url_app:home')
