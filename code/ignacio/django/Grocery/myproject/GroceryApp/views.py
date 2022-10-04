from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import GroceryItem
# Create your views here.
def homepage(request):
    objects = GroceryItem.objects.all()
    context = {
        'objects': objects
    }
    return render(request, 'GroceryApp/index.html', context)

def create(request):
    print(request.POST,"!!!!!!!!!!!!!!!!!!!!!!!!", type(request.POST["completed"]))
    item_name = request.POST['item_name']
    date_created = request.POST['date_created']
    completed = request.POST['completed']

    if completed == "True":
        completed = True
    else:
        completed = False

    grocerymodel = GroceryItem(item_name=item_name, date_created=date_created, completed=completed)
    grocerymodel.save()
    return redirect('GroceryApp:homepage')

def delete(request, id):
    item = get_object_or_404(GroceryItem, id=id)
    item.delete()
    return redirect('GroceryApp:homepage')

def edit_list(request, id):
    item = get_object_or_404(GroceryItem, id=id)
    item.completed = not item.completed
    item.save()
    return redirect('GroceryApp:homepage')
