from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from .models import UrlMeta, UrlLink
import random, string, urllib.parse

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
        while len(random_password) < 6:
            random_password.append(random.choice(random_char))
            random_display = ''.join(random_password)
        return random_display

def mycreate(request):
    content_length = request.META['CONTENT_LENGTH']
    csrf_cookie = request.META['CSRF_COOKIE']
    name = request.POST['name']
    url_long = request.POST['url_long']

    mytest = UrlMeta(name=name, content_length=content_length, csrf_cookie=csrf_cookie)
    mytest.save()
    mymodel = UrlLink(name=name, url_long=url_long, url_short=random_password(), url_meta=mytest)
    mymodel.save()

    return HttpResponseRedirect(reverse('url_shortener_app:home'))

def new_site(request, url_short):
    url = get_object_or_404(UrlLink, url_short=url_short)
    return HttpResponseRedirect(url.url_long)





