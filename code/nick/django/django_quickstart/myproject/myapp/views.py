from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import MyModel
from django.utils import timezone

def myview(request):
    myinstances = MyModel.objects.all()
    context = {
        'blogs': myinstances
    }
    return render(request, 'myapp/mytemplate.html', context)

def mycreate(request):
    author = request.POST['author']
    content = request.POST['content']
    timestamp = timezone.now()
    mymodel = MyModel(author=author, content=content, timestamp=timestamp)
    mymodel.save()
    return HttpResponseRedirect(reverse('myapp:myview'))