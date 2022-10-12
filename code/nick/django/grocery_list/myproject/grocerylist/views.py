from django.shortcuts import render, reverse, get_object_or_404, redirect
from .models import ToDoList
from datetime import date

def home(request):
    to_do_items = ToDoList.objects.all()
    context = {
        'to_do_list': to_do_items
    }
    return render(request, 'grocerylist/home.html', context)

def listcreation(request):
    grocery_genre = request.POST['grocery_genre']
    item_description = request.POST['item_description']
    completeBy_date = request.POST['completeBy_date']
    to_do_list = ToDoList(grocery_genre=grocery_genre, item_description=item_description, completeBy_date=completeBy_date)
    to_do_list.save()
    return redirect('grocerylist:home')

def myview(request):
    to_do_items = ToDoList.objects.all()
    context = {
        'to_do_list': to_do_items
    }
    return render(request, 'grocerylist/myview.html', context)

def edit_task(id):
    task_obj = get_object_or_404(ToDoList, id=id)
    task_obj.task_complete = not task_obj.task_complete
    task_obj.date_complete = date.today()
    task_obj.save()
    return redirect('grocerylist:myview')

def delete_task(id):
    task_obj = get_object_or_404(ToDoList, id=id)
    task_obj.delete()
    return redirect('grocerylist:myview')