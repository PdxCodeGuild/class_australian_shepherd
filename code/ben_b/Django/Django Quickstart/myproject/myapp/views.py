import re
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import MyModel

def home(request):
    myinstances = MyModel.objects.all()
    context = {
        'myinstances': myinstances
    }
    return render(request, 'myapp/mytemplate.html', context)

def mycreate(request):
    myfield = request.POST['myfield']
    mytext = request.POST['mytext']
    mymodel = MyModel(myfield=myfield, mytext=mytext)
    mymodel.save()
    return HttpResponseRedirect(reverse('myapp:home'))