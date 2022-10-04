from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
import random
import string

# Create your views here.
# def random_url():
#   length = 6
#   url = ''.join(random.choices(string.printable, k=length))
#   return url

def home(request):
  return HttpResponse('Make a tiny URL')
