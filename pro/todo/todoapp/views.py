from django.shortcuts import render
from django.http import HttpResponse, Http404
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
def detail(request, task_id): # Accepts task_id
    try:
        task = Task.objects.get(pk=task_id) # Filters out task to get requested
    except Task.DoesNotExist:
        raise Http404('Task does not exist')
    context = {
        'task': task,
    }
    return render(request, 'todoapp/detail.html', context) #Passes context into detail.html

    #Added exception handling functionality to detail view


