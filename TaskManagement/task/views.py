from django.views.generic import CreateView, ListView
from django.views.generic import DetailView
from django.views.generic.base import View
from task.models import Task
from task.forms import CreateTaskForm, CreateSubTaskForm
from project.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.core import serializers
# Create your views here.


class CreateTaskView(LoginRequiredMixin, CreateView):
    """ Display form where pm can create task and assign to employee."""
    model = Task
    template_name = 'task/add_task.html'
    form_class = CreateTaskForm


class CreateSubTaskView(LoginRequiredMixin, CreateView):
    """ Display form where pm can create subtask and assign to employee."""
    model = Task
    template_name = 'task/add_subtask.html'
    form_class = CreateSubTaskForm


class TaskListView(LoginRequiredMixin, ListView):
    """ Display list of tasks (for logged in user's list of tasks ) """
    model = Project
    template_name = "task/task_list.html"
    context_object_name = "tasklist"

    def get_queryset(self):
        print(self.request.GET.get("id"))
        id = self.request.GET.get("id")
        print(id)
        print(self.request.GET)
        #if project_id == "":
        #    Task.objects.none()
        return Project.objects.filter(project_lead=id)
    
    def get_context_data(self, **kwargs):
        project_list = []
        context = super(TaskListView, self).get_context_data(**kwargs)
        project_list = Project.objects.filter(project_lead=self.request.user)
        context['project'] = [project.title for project in project_list]
        return context

    #def get_queryset(self):
    #    # return Task.objects.filter(assigned_to=self.request.user)
    #    return Task.objects.filter(created_by__in=User.objects.filter(designation='Project Manager'))
        
    #def get_context_data(self, **kwargs):
    #    context = super(TaskListView, self).get_context_data(**kwargs)
    #    context['task'] = Task.objects.filter(assigned_to=self.request.user)
    #    return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    """Display detail of task."""
    model = Task
    template_name = "task/task_detail.html"
    context_object_name = "taskdetail"


class ProjectListView(View):

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            project = Project.objects.all()
            task_serializers = serializers.serialize('json', project)
            return JsonResponse(task_serializers, safe=False)
        return JsonResponse({'message' : 'wrong Validation'})
