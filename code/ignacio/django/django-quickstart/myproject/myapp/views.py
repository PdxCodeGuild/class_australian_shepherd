from multiprocessing import context
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def myview(request):
    return HttpResponse("test!")

from django.shortcuts import render

def myview(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'myapp/mytemplate.html', context)

from django.shortcuts import render
from .models import MyModel

def myview(request):
    myinstances = MyModel.objects.all()
    context = {
        'myinstances': myinstances
    }
    return render(request, 'myapp/mytemplate.html', context)

from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel

def myview(request):
    myinstances = MyModel.objects.all()
    context = {
        'myinstances': myinstances
    }
    return render(request, 'myapp/mytemplate.html', context)

def mycreate(request):
    print(request.POST)
    return HttpResponse('form received')

from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import MyModel

def myview(request):
    myinstances = MyModel.objects.all()
    context = {
        'myinstances': myinstances
    }
    return render(request, 'myapp/mytemplate.html', context)

def mycreate(request):
    myfield = request.POST['myfield']
    mymodel = MyModel(myfield=myfield)
    mymodel.save()
    return HttpResponseRedirect(reverse('myapp:myview'))