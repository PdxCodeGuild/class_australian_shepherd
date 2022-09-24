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
    myboolean = request.POST['myboolean']
    mytime = timezone.now()
    mymodel = MyModel(myfield=myfield, myboolean=myboolean, mytime=mytime)
    mymodel.save()
    return HttpResponseRedirect(reverse('myapp:myview'))