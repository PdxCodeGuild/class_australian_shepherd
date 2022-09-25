from django.shortcuts import render
from django.http import HttpResponse
from .models import GroceryModel

# Create your views here.
def myview(request):
    mygroceries = GroceryModel.objects.all()
    context = {
        'mygroceries': mygroceries
    }
    return render(request, 'grocery_list/grocerytemplate.html', context)
