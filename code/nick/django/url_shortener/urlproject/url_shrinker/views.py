from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from .models import ConvexURL
from random import choice
from string import ascii_letters, digits

# Create your views here.

def shrinker():
    new_url = ''
    for _ in range(6):
        new_url += choice(ascii_letters + digits)
    return new_url

def submitter(request):
    longURL = request.POST.get('longURL', False)
    short_url = shrinker()
    ConvexURL.objects.create(longURL=longURL, short_url=short_url)
    context = {
        'url_data': (ConvexURL.objects.last())
    }
    return render(request, 'url_shrinker/home.html', context)

def home(request):
    return render(request, 'url_shrinker/home.html')

def redirect_view(request, short_url):
    url_data = ConvexURL.objects.last()
    print(request.META['HTTP_REFERER'])
    return HttpResponseRedirect(url_data.longURL)