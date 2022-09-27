from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render, reverse
from django.utils import timezone
from .models import MyModel
from django.http import HttpResponseRedirect

def myview(request):
    myinstances = MyModel.objects.all()
    context = {
        'myinstances': myinstances
    }
    return render(request, 'myapp/mytemplate.html', context)

def mycreate(request):
    myfield = request.POST['myfield']
    author = request.POST['author']
    body = request.POST['body']
    timestamp = timezone.now()
    mymodel = MyModel(myfield=myfield, author=author, body=body, timestamp=timestamp)
    mymodel.save()
    return HttpResponseRedirect(reverse('myapp:myview'))
