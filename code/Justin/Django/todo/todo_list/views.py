from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import MyModel
from django.utils import timezone

# Create your views here.


def myview(request):
    my_data - MyModel.objects.all()
    context = {
        'messages': my_data
    }
    return render(request, 'todo_list/home.html', context)
