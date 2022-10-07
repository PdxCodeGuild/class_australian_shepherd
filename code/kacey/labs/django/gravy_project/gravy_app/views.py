from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    all_gravy = Post.objects.all()
    context = {
        'all_gravy' :                           
    }
    return render(request, '')