from django.shortcuts import render, redirect, get_object_or_404
from .models import GroceryList
from django.utils import timezone


def home(request):
    my_list = GroceryList.objects.all()
    context = {
        'my_lists': my_list
    }
    return render(request, 'groceryapp/home.html', context)

def create_list(request):
    grocery_item = request.POST['grocery_item']
    completed = request.POST['completed']
    completed_function = lambda x: True if x == 'True' else False
    completed = completed_function(completed)
    date = timezone.now()
    grocery_model = GroceryList(grocery_item=grocery_item, completed=completed, date=date)
    grocery_model.save()
    return redirect('groceryapp:home')

def edit_bool(request, id):
    list_object = get_object_or_404(GroceryList, id=id)
    list_object.completed = not list_object.completed
    list_object.save()
    return redirect('groceryapp:home')

def edit_grocery_item(request, id):
    list_object = get_object_or_404(GroceryList, id=id)
    if request.method == 'GET':
        context = {
            'movie': list_object
        }
        return render(request, 'groceryapp/edit_grocery_item.html', context)   
    elif request.method == 'POST':
        grocery_item = request.POST['grocery_item']
        list_object.grocery_item = grocery_item
        list_object.save()
        return redirect('groceryapp:home')

def delete_post(request, id):
    list_object = get_object_or_404(GroceryList, id=id)
    list_object.delete()
    return redirect('groceryapp:home')

