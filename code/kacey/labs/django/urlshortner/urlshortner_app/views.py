from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Urlshortner
from random import choice, randint
from string import ascii_letters
# Create your views here.
def homepage(request):
    all_urls = Urlshortner.objects.all()
    print(all_urls)
    context = {
        'urls' : all_urls
    }
    return render(request, 'urlshortner_app/homepage.html', context)

def new_url(request):
    code = ''
    while len(code) < 6:
        code += str(randint(0,9)) + choice(ascii_letters)
        
    long_url = request.POST['long_url']
    code_obj = Urlshortner(long_url=long_url, short_code = code)
    code_obj.save()
    
    return redirect("urlshortner_app:homepage")

def redirect_view(request, id):
    print(id, "!!!!!!!!!!!!!")
    url_obj = get_object_or_404(Urlshortner, id=id)
    # print(url_obj.long_url)
    # redirected_url = f"http://127.0.0.1:8000/{id}"
    return HttpResponseRedirect(url_obj.long_url) 
    
def delete_url():
    pass
