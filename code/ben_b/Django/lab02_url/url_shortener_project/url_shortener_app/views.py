from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import urlLink
import random, string

def home(request):
    myinstances = urlLink.objects.all()
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
    name = request.POST['name']
    url_long = request.POST['url_long']
    mymodel = urlLink(name=name, url_long=url_long, url_short=random_password())
    mymodel.save()
    return HttpResponseRedirect(reverse('url_shortener_app:home'))

def new_site(request, url_short):
    url = urlLink.url_long
    print(url, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    return HttpResponseRedirect(url)