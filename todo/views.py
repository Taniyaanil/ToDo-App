from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.urls import reverse

def task_list(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'todo/task_list.html', context)

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request, 'todo/add_task.html', context)

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('task_list')

def mark_done(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.done = True
    task.save()
    return redirect('task_list')
