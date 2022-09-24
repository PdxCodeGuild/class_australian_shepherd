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
    mytextfield = request.POST['mytextfield']
    author = request.POST['author']
    mymodel = MyModel(myfield=myfield, mytextfield=mytextfield, author=author)
    mymodel.save()
    return HttpResponseRedirect(reverse('myapp:myview'))