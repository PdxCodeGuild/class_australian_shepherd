from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Todo_list, Notes


def homepage(request):
    all_lists = Todo_list.objects.all()
    all_notes = Notes.objects.all()
    context = {"all_notes": all_notes, "all_lists": all_lists}
    return render(request, "todo_list_app/todo.html", context)


def new_objective(request):
    title = request.POST["title"]
    objective = request.POST["objective"]
    start_date = request.POST["start_date"]
    in_progress = bool(request.POST["in_progress"])
    priority = request.POST["priority"]

    todo_list_object = Todo_list(
        title=title,
        objective=objective,
        start_date=start_date,
        in_progress=in_progress,
        priority=priority,
    )
    todo_list_object.save()
    print(type(todo_list_object))

    return redirect("todo_list_app:homepage")


def edit_objective(_, id):
    todo_list_obj = get_object_or_404(Todo_list, id=id)
    todo_list_obj.in_progress = not todo_list_obj.in_progress
    todo_list_obj.save()
    return redirect("todo_list_app:homepage")


def new_note(request):
    note = request.POST["note"]

    note_obj = Notes(note=note)
    note_obj.save()

    return redirect("todo_list_app:homepage")


def delete_note(request, id):
    note_obj = get_object_or_404(Notes, id=id)
    note_obj.delete()

    return redirect("todo_list_app:homepage")
