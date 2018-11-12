from django.shortcuts import render
from todo.models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})
    
def new(request):
    
    return render(request, 'todo/new.html')