from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Biz

import random

# just to show this is python and we can treat it that way
def name_random_phone_number():
    return str(random.randint(1000000000, 9999999999))

def home(request):
    all_biz = Biz.objects.all()
    context = {
        'shops': all_biz
    }

    return render(request, 'biz_app/base.html', context)

def addsite(request):
    if request.method == 'POST':
        name = request.POST['name']

        # phone = request.POST['phone']
        phone = name_random_phone_number() # purely to show that we can do normal python and logic

        email = request.POST['email']
        url = request.POST['url']
        Biz.objects.create(name=name, phone=phone, email=email, website=url)
        return redirect( 'biz_app:addsite')
    else:
        all_biz = Biz.objects.all()
        context = {
            'shops': all_biz
        }
    return render(request, 'biz_app/addwebsite.html', context)


def redirect_view(request, name):
    # new_url = get_object_or_404(Biz, website=name)
    print(name, "!!!!!!!!!!!!!!!!!!!!!!!!")
    url = 'https://www.google.com/search?q=' + name + '&tbm=isch&ved=2ahUKEwi7lI7QscX6AhVQHTQIHb6hCzwQ2-cCegQIABAA&oq=dogs&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIFCAAQgAQyCAgAEIAEELEDMgsIABCABBCxAxCDATIICAAQgAQQsQMyBQgAEIAEMggIABCABBCxAzIICAAQgAQQsQM6BAgjECc6CQgAEIAEEAoQGDoHCAAQgAQQGDoICAAQsQMQgwFQgQZY-glg8ApoAHAAeACAATOIAfUBkgEBNZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=nIc7Y7vWHdC60PEPvsOu4AM&bih=1030&biw=1064&rlz=1C1ONGR_enUS969US969'

    return HttpResponseRedirect(url)