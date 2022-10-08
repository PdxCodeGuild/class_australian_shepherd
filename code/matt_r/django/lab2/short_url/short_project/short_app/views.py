from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Short
import random
import string



letters = string.ascii_letters
digits = string.digits
all_char = letters + digits



def new_url():
    temp_str = ''
    while len(temp_str) < 5:
        temp_str = temp_str + random.choice(all_char)
    return temp_str

def home(request):
    full_url = Short.objects.all()
    context = {
        'urls': full_url
    }

    if request.method == 'POST':
        website = request.POST['website']

        short_url = new_url()
        Short.objects.create(website=website, short_url=short_url)

        print(website, "@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

        return redirect('short_app:home')

    else:   
        return render(request, 'short_app/home.html', context)

    




def redirect_view(request, id):
    short_obj = get_object_or_404(Short,id=id)
    
    print(short_obj, '?????????????????????????????????????')
    return HttpResponseRedirect(short_obj.website)





    