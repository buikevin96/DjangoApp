from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.

def index(request):
    task_list = Task.objects.all() # Retrieve all the objects from the task model
    output = ','.join([q.task_priority for q in task_list])
    return HttpResponse(output)

def detail(request):
    return HttpResponse('This is the detail view')

