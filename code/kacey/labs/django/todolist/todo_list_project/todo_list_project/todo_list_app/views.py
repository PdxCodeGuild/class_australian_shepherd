from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Todo_list


def homepage(request):
    all_list = Todo_list.objects.all()
    context = {
        'all_lists': all_list
    }
    return render(request, 'todo_list_app/todo.html', context)


def new_objective(request):

    title = request.POST['title']
    objective = request.POST['objective']
    start_date = request.POST['start_date']
    in_progress = bool(request.POST['in_progress'])

    todo_list_model = Todo_list(title=title, objective=objective, start_date=start_date, in_progress=in_progress)
    todo_list_model.save()

    return redirect('todo_list_app:homepage')


def edit_objective(request, id):
    todo_list_obj = get_object_or_404(Todo_list, id=id)
    todo_list_obj.in_progress = not todo_list_obj.in_progress
    todo_list_obj.save()
    return redirect('todo_list_app:homepage')

