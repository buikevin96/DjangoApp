from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.

def index(request):
    task_list = Task.objects.all() # Retrieve all the objects from the task model
    output = ','.join([q.task_name for q in task_list])# Retrieve all of the task_names in the task_list and append a comma after them
    return HttpResponse(output)

def detail(request, task_id):
    return HttpResponse('This is task number %s' % task_id)

