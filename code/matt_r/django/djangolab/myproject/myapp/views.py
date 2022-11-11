from urllib import request
from django.shortcuts import render 

# Create your views here.

from django.http import HttpResponse

def myview(request):
    return HttpResponse('hello world!')