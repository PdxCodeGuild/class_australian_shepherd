from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Todo_List


def homepage(request):
    all_list = Todo_List.objects.all()
    context = {
        'all_lists': all_list
    }
    return render(request, 'todo_list_app/home.html', context)


def new_objective(request):

    title = request.POST['title']
    objective = request.POST['objective']
    start_date = request.POST['start_date']
    in_progress = bool(request.POST['in_progress'])

    todo_list_model = Todo_List(title=title, objective=objective, start_date=start_date, in_progress=in_progress)
    todo_list_model.save()

    return redirect('todo_list_app:homepage')


def edit_objective(request, id):
    todo_list_obj = get_object_or_404(Todo_List, id=id)

    todo_list_obj.in_theatres = not todo_list_obj.in_theatres
    todo_list_obj.save()
    return redirect('todo_list_app:homepage')

