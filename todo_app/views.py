# coding: utf-8
from datetime import date
from django.http import HttpResponse
from django.shortcuts import render
from todo_app.models import Task


def index(request):
    tasks_list = Task.objects.order_by('-due_date')
    for task in tasks_list:
        if task.get_due_date():
            task.overdue = task.get_due_date() < date.today()
    context = {'tasks_list': tasks_list}
    return render(request, 'todo_app/index.html', context)


# class IndexView(generic.ListView):
#     template_name = 'todo_app/index.html'
#     context_object_name = 'tasks_list'
#
#     def get_queryset(self):
#         return Task.objects.order_by('-due_date')


def check_task_done(request):
    task_id = None
    if request.method == 'GET':
        task_id = request.GET['task_id']

    if task_id:
        task = Task.objects.get(id=int(task_id))
        if task:
            task.is_done = not task.is_done
            task.save()
            if task.get_due_date():
                task.overdue = task.get_due_date() < date.today()
            context = {'task': task}
            return render(request, 'todo_app/task_text.html', context)
    return HttpResponse()


def add_new_task(request):
    if request.method == 'GET':
        new_task_text = request.GET['task_text']

        if new_task_text:
            new_task_date = request.GET['task_date']
            if new_task_date:
                task = Task(task_text=new_task_text, due_date=new_task_date)
            else:
                task = Task(task_text=new_task_text)
            task.save()
            context = {'task': task}
            return render(request, 'todo_app/task.html', context)
    return HttpResponse()
