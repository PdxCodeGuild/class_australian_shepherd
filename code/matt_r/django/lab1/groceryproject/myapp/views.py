from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import grocerys

def homeview(request):
    all_items = grocerys.objects.all()
    context = {
        'all_items': all_items
    }

    return render(request, 'myapp/home.html', context)


def new_item(request):
    print(request.POST, '!!!!!!!!!!!!!!!!!!')
   
    item = request.POST['item']
    quanity = request.POST['quanity']
    date_created = request.POST['date']
    completed = request.POST['complete']
    if completed == 'True':
        completed = True
    else:
        completed = False

    grocery_model = grocerys(item=item, date_created=date_created, completed=completed, quanity=quanity)
    grocery_model.save()

    return redirect('myapp:home')



def edit_item(request, id):

    item_obj = get_object_or_404(grocerys, id=id)

    item_obj.completed = not item_obj.completed
    item_obj.save()
    return redirect('myapp:home')

def delete_item(request, id):
    item_obj = get_object_or_404(grocerys, id=id)
    item_obj.delete()

    return redirect('myapp:home')