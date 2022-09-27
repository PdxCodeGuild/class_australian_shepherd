from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import GroceryModel

# Create your views here.
def myview(request):
    mygroceries = GroceryModel.objects.all()
    context = {
        'mygroceries': mygroceries
    }
    return render(request, 'grocery_list/grocerytemplate.html', context)

def mycreate(request):
    GroceryItem = request.POST['GroceryItem']
    grocerymodel = GroceryModel(GroceryItem=GroceryItem)
    grocerymodel.save()
    return HttpResponseRedirect(reverse('grocery_list:myview'))
