from django.shortcuts import render, redirect
from .models import GroceryList

def home(request):
    my_lists = GroceryList.objects.all()
    context = {
        'my_lists': my_lists
    }
    return render(request, 'groceryapp/home.html', context)

def create_list(request):
    grocery_item = request.POST['grocery_item']
    mymodel = GroceryList(grocery_item=grocery_item)
    mymodel.save()
    return redirect('groceryapp:home')