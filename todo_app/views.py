from django.shortcuts import render
from todo_app.models import Task


def index(request):
    tasks_list = Task.objects.order_by('-due_date')
    context = {'tasks_list': tasks_list}
    return render(request, 'todo_app/index.html', context)