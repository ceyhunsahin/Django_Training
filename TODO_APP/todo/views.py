from django.shortcuts import render
# from .models import Todo_Model
from .models import Todo
def home(request) :
    return render(request, "pages/home.html")

def todo_list(request) :
    todos = Todo.objects.all()
    context = {
        'todos' : todos
    }
    return render(request, 'pages/todo_list.html', context)
# Create your views here.
