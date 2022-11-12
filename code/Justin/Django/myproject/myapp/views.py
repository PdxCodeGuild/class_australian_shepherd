from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from .models import MyModel
from django.utils import timezone


def myview(request):
    my_data = MyModel.objects.all()
    context = {
        'messages': my_data
    }
    return render(request, 'myapp/home.html', context)


def mycreate(request):
    myfield = request.POST['myfield']
    myauthor = request.POST['myauthor']
    created = timezone.now()
    mymodel = MyModel(myfield=myfield, myauthor=myauthor, created=created)
    mymodel.save()
    return HttpResponseRedirect(reverse('myapp:home'))


def detail(request, pk):
    my_data = get_object_or_404(MyModel, pk=pk)
    context = {
        'message': my_data
    }
    print('\n', pk)
    return render(request, 'myapp/detail.html', context)
