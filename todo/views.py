from django.shortcuts import render, redirect
from todo.models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})
    
def new(request):
    # 사용자가 입력할 수 있는 폼을 만들어주기
    return render(request, 'todo/new.html')
    
def create(request):
    title = request.POST.get('title')
    deadline = request.POST.get('deadline')
    todo = Todo(title=title, deadline=deadline)
    todo.save()
    return redirect('/todos/')
    
def read(request, id):
    todo = Todo.objects.get(id=id)
    return render(request, 'todo/read.html', {'todo': todo})