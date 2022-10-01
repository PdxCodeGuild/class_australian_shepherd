from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import TinyUrl
from random import choice
from string import ascii_letters, digits

def generator():
    url = ''
    for _ in range(6):
        url += choice(ascii_letters + digits)

    return url


def home(request):
    if request.method == 'POST':
        long_url = request.POST['long_url']
        short_url = generator()
        TinyUrl.objects.create(long_url=long_url, short_url=short_url)
        context = {
            'urls': TinyUrl.objects.all()
        }
        return render(request, 'tiny_url_app/home.html', context)
    else:
        all_movie = TinyUrl.objects.all()
        context = {
            'urls': all_movie
        }

        return render(request, 'tiny_url_app/home.html', context)


def redirect(request, short_url):
    new_url = get_object_or_404(TinyUrl, short_url=short_url)
    return HttpResponseRedirect(new_url.long_url)