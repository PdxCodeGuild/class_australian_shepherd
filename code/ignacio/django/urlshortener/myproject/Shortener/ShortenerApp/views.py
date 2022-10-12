from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import shrink
import random, string

def scrabble(request):
    short_url = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(7))
    return short_url
    

def homepage(request):
    objects = shrink.objects.all()
    context = {
        'objects': objects
    }
    return render(request, 'shortener_app/index.html', context)


def create(request):
    url = 
    short_url = scrabble()
    

    return HttpResponseRedirect(reverse('shortener_app:homepage'))