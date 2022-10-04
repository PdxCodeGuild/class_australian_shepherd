from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Url
import random, string

def home(request):
    urls = Url.objects.all()
    context = {
        'urls': urls
    }
    return render(request, 'urlshort_app/index.html', context)

def shorten(request):
        if request.method == 'POST':

            url = request.POST['url']
            short = ''.join(random.choice(string.ascii_letters) for x in range(5))
            new = Url(url=url, short=short)
            new.save()

            return HttpResponseRedirect(reverse('urlshort_app:home'))