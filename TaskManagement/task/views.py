from accounts.models import Designation, User
from django.shortcuts import render
from django.views.generic import CreateView,ListView
from task.models import TASKTYPES, Task
from task.forms import CreateTaskForm
# Create your views here.

class CreateTaskView(CreateView):
    """ Display form where pm can create task and assign to employee."""
    model = Task
    template_name = 'employee/add_task.html'
    form_class = CreateTaskForm
    


class TaskListView(ListView):
    """ Display list of tasks """
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasklist"

    def get_queryset(self):
        return Task.objects.filter(status='2')