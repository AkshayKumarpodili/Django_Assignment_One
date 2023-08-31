from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fun(request):
    return HttpResponse("Hello World!!")

def task_page(request):
    return render(request, 'task.html', {'name': 'Akshay'})
