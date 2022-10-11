from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import MyModel
from django.utils import timezone


def myview(request):
    my_data = MyModel.objects.all()
    return render(request, 'myapp/home.html')


def mycreate(request):
    myfield = request.POST['myfield']
    myauthor = request.POST['myauthor']
    created = timezone.now()
    mymodel = MyModel(myfield=myfield, myauthor=myauthor, created=created)
    mymodel.save()
    return HttpResponseRedirect(reverse('myapp:home'))
