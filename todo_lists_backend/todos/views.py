from django.http      import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls      import reverse

from .models import TodoList, Todo

def index(request):
    todo_lists = TodoList.objects.all()
    context = { "todo_lists": todo_lists }
    return render(request, "todos/index.html", context)

def todo_list(request, list_id):
    todo_list = get_object_or_404(TodoList, pk=list_id)
    todos = todo_list.todo_set.all()
    context = {
        "todo_list": todo_list,
        "todos": todos,
    }
    return render(request, "todos/todo_list.html", context)

def new(request, list_id):
    todo_list = get_object_or_404(TodoList, pk=list_id)
    if request.method == "GET":
        context = { "todo_list": todo_list }
        return render(request, "todos/new.html", context)
    elif request.method == "POST":
        description = request.POST["description"]
        todo_list.todo_set.create(description=description)
        
        return HttpResponseRedirect(f'/{todo_list.id}')

def edit_todo(request, list_id, todo_id):
    context = request.POST
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.is_complete = True if context["is_complete"] == "true" else False
    todo.save()
    return HttpResponse()

def api_lists(request):
    lists = list(TodoList.objects.all().values())
    return JsonResponse(lists, safe=False)

def api_list(request, list_id):
    todo_list = get_object_or_404(TodoList, pk=list_id)
    todos = todo_list.todo_set.all().values()

    list_data = {
        'title': todo_list.title,
        'pub_date': todo_list.pub_date,
        'todos': list(todos),
    }

    return JsonResponse(list_data, safe=False)