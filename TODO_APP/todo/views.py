from django.shortcuts import render, redirect,get_object_or_404
# from .models import Todo_Model
from .models import Todo
from .forms import TodoUpdateForm, TodoAddForm
def home(request) :
    return render(request, "pages/home.html")

def todo_list(request) :
    todos = Todo.objects.all()
    context = {
        'todos' : todos
    }
    return render(request, 'pages/todo_list.html', context)
# Create your views here.

def todo_create(request) :
    form = TodoAddForm()
    if request.method == 'POST':
        form = TodoAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        else :
            form = TodoAddForm()
    context = {
        'form' : form
    }
    return render(request, 'pages/todo_created.html', context)

def todo_update(request, id):
    todo = get_object_or_404(Todo, id = id)
    form = TodoUpdateForm(instance=todo)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'todo' : todo,
        'form' : form
    }
    return render(request, "pages/todo_update.html", context)

def todo_delete(request,id):
    todo = get_object_or_404 (Todo, id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect ('list')
    context = {
        'todo' : todo,
    }
    return render (request, "pages/todo_delete.html",context)

