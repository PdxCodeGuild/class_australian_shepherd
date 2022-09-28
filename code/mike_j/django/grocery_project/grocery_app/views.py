from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import GroceryItem
from django.utils import timezone

def home(request):
    items = GroceryItem.objects.all()
    context = {
        'items': items
    }
    return render(request, 'grocery_app/index.html', context)

def add_item(request):
    item = request.POST['item'] 
    timestamp = timezone.now()
    complete = request.POST['complete']  
    mymodel = GroceryItem(item=item, timestamp=timestamp, complete=complete)
    mymodel.save()
    return HttpResponseRedirect(reverse('grocery_app:home'))