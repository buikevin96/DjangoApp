from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.template import loader

# Create your views here.

def index(request):
    task_list = Task.objects.all() # Retrieve all the objects from the task model
    # template = loader.get_template('todoapp/index.html')
    context = {

        'task_list': task_list
    }
    #output = ','.join([q.task_name for q in task_list])# Retrieve all of the task_names in the task_list and append a comma after them
    return render(request, 'todoapp/index.html', context)

# Detail View
def detail(request, task_id):
    task = Task.objects.get(pk=task_id)
    context = {
        'task': task,
    }
    return render(request, 'todoapp/detail.html', context)


