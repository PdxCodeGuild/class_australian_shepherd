from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import GroceryItem
from django.utils import timezone

# Create your views here.


def myview(request):
    g_list = GroceryItem.objects.all()
    context = {
        'message': g_list
    }
    return render(request, 'myapp/home.html', context)


def MyItems(request):
    item_name = request.POST['item_name']
    requestor = request.POST['requestor']
    item_description = request.POST['item_description']
    created = timezone.now()
    completed = False
    mymodel = GroceryItem(item_name=item_name, requestor=requestor,
                          created=created, item_description=item_description, completed=completed)
    mymodel.save()
    return HttpResponseRedirect(reverse('myapp:home'))


def Completed(request, pk):
    grocery_item = get_object_or_404(GroceryItem, pk=pk)
    grocery_item.completed = not bool(grocery_item.completed)
    grocery_item.save()
    return HttpResponseRedirect(reverse('myapp:home'))


def Delete_Item(request, id):
    item = GroceryItem.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect(reverse('myapp:home'))
