from django.shortcuts import render
import random


# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def lunch(request):
    menu_list = ['20층', '깁밥카페', '시골집']
    pick = random.choice(menu_list)
    return render(request, 'lunch.html', {'pick': pick})
    
def lotto(request):
    num_list = list(range(1, 46, 1))
    picks = random.sample(num_list, 5)
    return render(request, 'lotto.html', {'picks': picks})
    
def hello(request, name):
    return render(request, 'hello.html', {'name': name})
    
def cube(request, num):
    num_cube = num ** 3
    return render(request, 'cube.html', {'num_cube': num_cube})