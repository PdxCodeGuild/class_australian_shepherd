from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import GroceryModel
from django.utils import timezone

# Create your views here.
def myview(request):
    mygroceries = GroceryModel.objects.all()
    context = {
        'mygroceries': mygroceries
    }
    return render(request, 'grocery_list/grocerytemplate.html', context)

def mycreate(request):
    GroceryItem = request.POST['GroceryItem']
    DateAdded = timezone.now()
    ToDo = request.POST['ToDo']
    grocerymodel = GroceryModel(GroceryItem=GroceryItem, DateAdded=DateAdded, ToDo=ToDo)
    grocerymodel.save()
    return HttpResponseRedirect(reverse('grocery_list:myview'))
