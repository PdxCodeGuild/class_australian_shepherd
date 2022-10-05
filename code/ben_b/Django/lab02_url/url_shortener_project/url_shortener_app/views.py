from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from .models import UrlMeta, UrlLink
import random, string

def home(request):
    myinstances = UrlLink.objects.all()
    context = {
        'myinstances': myinstances
    }
    return render(request, 'url_shortener_app/home.html', context)

def random_password():
        random_char = string.ascii_letters + string.digits + string.punctuation
        random_password = []
        random_display = ''
        x = 6
        while len(random_password) < x:
            random_password.append(random.choice(random_char))
            random_display = ''.join(random_password)
        return random_display

def mycreate(request):
    meta = request.META.keys()

    print(request.META, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    name = request.POST['name']
    url_long = request.POST['url_long']
    mymodel = UrlLink(name=name, url_long=url_long, url_short=random_password())
    dummy_data = UrlLink.objects.all()
    dummy_data.save()
    mytest = UrlMeta(meta=meta, url_meta=dummy_data)
    mymodel.save()
    mytest.save()

    return HttpResponseRedirect(reverse('url_shortener_app:home'))

def new_site(request, url_short):
    url = get_object_or_404(UrlLink, url_short=url_short)
    return HttpResponseRedirect(url.url_long)

def parse_meta(request):
    return request.META.keys()




