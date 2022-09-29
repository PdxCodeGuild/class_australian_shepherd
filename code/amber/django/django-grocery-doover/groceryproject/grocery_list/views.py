from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myview(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'grocery_list/mytemplate.html', context)
