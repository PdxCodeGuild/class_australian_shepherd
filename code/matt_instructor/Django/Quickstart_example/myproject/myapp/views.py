from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .models import MyModel
from django.utils import timezone
from .forms import PostForm

def home(request):
    my_data = MyModel.objects.all()
    context = {
        'messages': my_data
    }
    return render(request, 'myapp/home.html', context)

def mycreate(request):
    myfield = request.POST['myfield']
    author = request.POST['author']
    pub_date =  timezone.now()

    mymodel = MyModel(myfield=myfield, author=author, pub_date=pub_date)

    mymodel.save()
    print('\n', )
    return HttpResponseRedirect(reverse('myapp:home'))

def detail(request, pk):
    my_data = get_object_or_404(MyModel, pk=pk)
    context = {
        'message': my_data
    }
    
    return render(request, 'myapp/detail.html', context)


