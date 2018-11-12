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
    
def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        deadline = request.POST.get('deadline')
        # todo = Todo(title=title, deadline=deadline)
        # todo.save()
        Todo.objects.create(title=title, deadline=deadline)
        return redirect('/todos/')
    return render(request, 'todo/todo_create.html')
    
def read(request, id):
    todo = Todo.objects.get(id=id)
    deadline = todo.deadline.strftime("%Y-%m-%d")
    return render(request, 'todo/read.html', {'todo': todo,'deadline':deadline})
    
def delete(request, id):
    Todo.objects.get(id=id).delete()
    return redirect('/todos/')
    
def update(request, id):
    todo = Todo.objects.get(id=id)
    deadline = todo.deadline.strftime("%Y-%m-%d")
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.deadline = request.POST.get('deadline')
        todo.save()
        return redirect('/todos/')
    return render(request, 'todo/update.html', {'todo': todo, 'deadline': deadline})