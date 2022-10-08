from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import shrink
import random, string

def scrabble():
    rando_letter = ''.join(random.choice(string.ascii_letters) for x in range(7))
    return rando_letter

def homepage(request):
    objects = shrink.objects.all()
    context = {
        'objects': objects
    }
    return render(request, 'ShortenerApp/index.html', context)


def transport(request):
        if request.method == 'POST':
            short_url = scrabble
            url = request.POST['url']

            return HttpResponseRedirect(reverse('ShortenerApp:homepage'))