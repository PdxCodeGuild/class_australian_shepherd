from django.shortcuts import render
from django.utils import timezone

def myview(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'myapp/mytemplate.html', context)
