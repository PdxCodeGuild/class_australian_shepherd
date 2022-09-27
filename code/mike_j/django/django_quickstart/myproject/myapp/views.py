from email import utils
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import MyModel
from django.utils import timezone

def myview(request):
    myinstances = MyModel.objects.all()
    context = {
        'myinstances': myinstances
    }
    return render(request, 'myapp/mytemplate.html', context)

def mycreate(request):
    myfield = request.POST['myfield']
    mytextfield = request.POST['mytextfield']
    author = request.POST['author']
    timestamp = timezone.now()
    mymodel = MyModel(myfield=myfield, mytextfield=mytextfield, author=author, timestamp=timestamp)
    mymodel.save()
    return HttpResponseRedirect(reverse('myapp:myview'))