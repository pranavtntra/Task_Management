from project.models import Project, ProjectTeam
from task.models import Task
from django.views.generic import CreateView, ListView, View, DetailView
from task.forms import CreateTaskForm, CreateSubTaskForm
from django.http import JsonResponse
import json
from django.shortcuts import render
from django.db.models import Q
import logging
from task.mixins import PassRequestToFormViewMixin
from django.core.serializers.json import DjangoJSONEncoder
import datetime
# Create your views here.


class CreateTaskView(PassRequestToFormViewMixin, CreateView):
    """ Display form where pm can create task and assign to employee."""

    form_class = CreateTaskForm
    template_name = 'task/add_task.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(CreateTaskView, self).form_valid(form)

# def load_teammate(request):
#     project_id = request.GET.get('project')
#     # import code; code.interact(local=dict(globals(), **locals()))
#     assign = Project.objects.filter(project = project_id)
                
#     assigned_to = ProjectTeam.objects.filter(id=assign.teammate.id)
                #ProjectTeam.objects.filter(project=project_id).values('teammate__first_name')
#     return render(request, 'task/load_teammate.html', {'assigned_to': assigned_to})
  

class CreateSubTaskView(PassRequestToFormViewMixin, CreateView):
    """ Display form where employee can create subtask."""
    model = Task
    form_class = CreateSubTaskForm
    template_name = 'task/add_subtask.html'
    initial = {'start_date': datetime.date.today()}

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.assigned_to = self.request.user
        return super(CreateSubTaskView, self).form_valid(form)


def load_project(request):
    """for load project when parent task is selected in subtask form"""
    if request.is_ajax:
        task_id = request.GET.get('task_id')
        task = Task.objects.get(id=task_id)
        projects = Project.objects.filter(id=task.project.id) if task else Project.objects.none()
    return render(request, 'task/load_project.html', {'projects': projects})


class TaskListView(ListView):
    """ Display list of tasks (for logged in employee's list of tasks ) """
    model = Task
    template_name = "task/mytask_list.html"
    context_object_name = "tasklist"

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user).order_by('-id')


class TaskDetailView(DetailView):
    """ Display task in detail(for logged in employee) """
    model = Task
    template_name = 'task/task_detail.html'
    context_object_name = "task_detail"


class ProjectTaskListView(ListView):
    """Display list of project so that we can select it and get list"""
    model = Project
    form_class = CreateTaskForm
    template_name = "task/project_tasklist.html"
    context_object_name = "projectlist"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Project.objects.all()
        else:
            return Project.objects.filter(project_lead=self.request.user)


class TaskList(View):
    """Display list of tasks in selected project."""
    model = Project
    form_class = CreateTaskForm
    template_name = "task/project_tasklist.html"
    context_object_name = "tasklist"

    def get(self, request):
        try:
            project_id = self.request.GET.get('id', None)
            project_id = Project.objects.filter(id=project_id)
            if project_id.exists():
                project = project_id.first()
                task_list = Task.objects.filter(project=project).values('title', 'assigned_to__first_name', 'status', 'priority', 'tasktype', 'start_date', 'end_date')
            tasks = json.dumps(list(task_list), cls=DjangoJSONEncoder)
            data = {"task": tasks}
            return JsonResponse(data, safe=False)
        except Exception as e:
            logging.error(str(e))


class SearchTaskView(View):
    """for search task in all the tasks"""
    def get(self, request):
        try:
            project_id = self.request.GET.get('id', None)
            project = Project.objects.filter(id=project_id).last()
            search = self.request.GET.get('search_here', None)
            print(project)
            print(search)
            task_list = Task.objects.filter(project=project)
            task = task_list.filter(Q(title__icontains=search) |
                                    Q(assigned_to__first_name__icontains=search) |
                                    Q(priority__icontains=search) |
                                    Q(tasktype__icontains=search)).order_by('-id')
            data = {"task": task,
                    "error_message": "there is no task."}
            return render(request, 'task/search_list.html', data)
        except Exception as e:
            logging.error(str(e))


class TaskListBetweenDates(View):
    """ Display task in range of selected dates"""
    def get(self, request):
        try:
            start_date = self.request.GET.get('start_date')
            end_date = self.request.GET.get('end_date')
            task = Task.objects.filter(start_date=start_date)
            data = {"task": task}
            return render(request, "task/project_tasklist.html", data)
        except Exception as e:
            logging.error(str(e))
            return render(request, 'dashboard.html')
