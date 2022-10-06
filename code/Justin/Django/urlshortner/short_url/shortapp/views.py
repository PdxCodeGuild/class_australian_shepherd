from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import ShortenedURL
import random
import string

# Create your views here.


def shortapp(request):
    url_info = ShortenedURL.objects.all()
    context = {
        'message': url_info
    }
    return render(request, 'shortapp/index.html', context)


def codeURL(request):
    long_url = request.POST['long_url']
    short_url = ''.join(random.choice(string.ascii_letters + string.digits)
                        for _ in range(6))
    mymodel = ShortenedURL(long_url=long_url, short_url=short_url)
    mymodel.save()
    url_info = ShortenedURL.objects.all()
    context = {
        'message': url_info
    }
    return render(request, 'shortapp/index.html', context)


def RedirURL(request, id):
    new_url = get_object_or_404(ShortenedURL, id=id)
    # return new_url
    return HttpResponseRedirect(new_url.long_url)
