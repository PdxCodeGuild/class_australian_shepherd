from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import GroceryModel

# Create your views here.
def myview(request):
    mygroceries = GroceryModel.objects.all()
    context = {
        'mygroceries': mygroceries
    }
    return render(request, 'grocery_list/grocerytemplate.html', context)

def add_item(request):
    print('!!!!!!!!!!!!!!!!!!!!!!!!!', request.POST)
    groceryitem = request.POST['groceryitem']
    dateadded = timezone.now()
    todo = False
    grocerymodel = GroceryModel(groceryitem=groceryitem, dateadded=dateadded, todo=todo)
    grocerymodel.save()
    return redirect('grocery_list:myview')

def complete(request, id):
    groceryitem = get_object_or_404(GroceryModel, id=id)
    groceryitem.todo = not groceryitem.todo
    groceryitem.save()
    return redirect('grocery_list:myview')

def delete_item(request, id):
    groceryitem = get_object_or_404(GroceryModel, id=id)
    groceryitem.delete()
    return redirect('grocery_list:myview')
