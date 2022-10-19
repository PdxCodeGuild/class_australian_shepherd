from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from .models import Url
import random, string

def home(request):
    urls = Url.objects.all()
    context = {
        'urls': urls
    }
    return render(request, 'urlshort_app/index.html', context)

def shorten():
        
    short_code = ''.join(random.choice(string.ascii_letters) for x in range(5))

    return short_code

def add_url(request):

    url = request.POST['url']
    short = shorten()
    new = Url(url=url, short=short)
    new.save()

    return redirect('urlshort_app:home')

def sendview(request, id):
    link = get_object_or_404(Url, id=id)
    data = link.url     

    return HttpResponseRedirect(data) 