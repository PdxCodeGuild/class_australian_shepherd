from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, reverse
from .models import shrink
import random, string

def scrabble():
    short_url = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(7))
    return short_url
    

def homepage(request):
    objects = shrink.objects.all()
    context = {
        'urls': objects
    }
    return render(request, 'shortener_app/index.html', context)


def create(request):
    long_url = request.POST.get('url')
    short_url = scrabble()
        
    url = shrink(url = long_url, short_url = short_url)
    url.save()
    return HttpResponseRedirect(reverse('shortener_app:homepage'))

def redirect_view(request, id):
    
    url_obj= get_object_or_404(shrink, id=id)
    # print(url_obj.)
    return HttpResponseRedirect(url_obj.url)