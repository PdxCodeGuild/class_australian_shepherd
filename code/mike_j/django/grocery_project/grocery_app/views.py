from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import GroceryItem
from django.utils import timezone

def home(request):
    items = GroceryItem.objects.all()
    context = {
        'items': items
    }
    return render(request, 'grocery_app/index.html', context)

def add(request):
    item = request.POST['item'] 
    timestamp = timezone.now()
    complete = request.POST['complete']  
    mymodel = GroceryItem(item=item, timestamp=timestamp, complete=complete)
    mymodel.save()
    return HttpResponseRedirect(reverse('grocery_app:home'))

def delete(request, id):
    item = get_object_or_404(GroceryItem, id=id)
    item.delete()
    return redirect('grocery_app:home')

def edit(request, id):
    item = get_object_or_404(GroceryItem, id=id)
    item.complete = not item.complete
    item.save()
    return redirect('grocery_app:home')    