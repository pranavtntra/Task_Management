from django.views.generic.edit import UpdateView
from project.models import Project
from task.models import Task
from django.views.generic import CreateView, ListView, View, DetailView
from task.forms import CreateTaskForm, CreateSubTaskForm
from django.http import JsonResponse
from django.shortcuts import render
import logging
from task.mixins import PassRequestToFormViewMixin
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from task.services import get_tasklist, search_task, search_task_by_dates
# Create your views here.


class CreateTaskView(LoginRequiredMixin, PassRequestToFormViewMixin, CreateView):
    """ Display form where pm can create task and assign to employee."""

    form_class = CreateTaskForm
    template_name = 'task/add_task.html'
    initial = {'start_date': datetime.date.today()}

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(CreateTaskView, self).form_valid(form)


class CreateSubTaskView(LoginRequiredMixin, PassRequestToFormViewMixin, CreateView):
    """ Display form where employee can create subtask."""
    model = Task
    form_class = CreateSubTaskForm
    template_name = 'task/add_subtask.html'
    initial = {'start_date': datetime.date.today()}

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.assigned_to = self.request.user
        return super(CreateSubTaskView, self).form_valid(form)


def load_task(request):
    """load task when project is selected in subtask form"""
    project_id = request.GET.get('project_id')
    print(project_id)
    parent_t = Task.objects.filter(project=project_id)
    parent_task = parent_t.filter(assigned_to=request.user)
    data = []
    [data.append({'id': task.id, 'title': task.title}) for task in parent_task]
    return JsonResponse(data, safe=False)


class TaskListView(LoginRequiredMixin, ListView):
    """ Display list of tasks (for logged in employee's list of tasks ) """
    model = Task
    template_name = "task/mytask_list.html"
    context_object_name = "tasklist"

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user).order_by('-id') and Task.objects.filter(parent_task=None)


class TaskSubListView(LoginRequiredMixin, ListView):
    """ Display list of tasks (for logged in employee's list of tasks ) """
    model = Task
    template_name = "task/mysubtask_list.html"
    context_object_name = "subtasklist"

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)


class TaskDetailView(LoginRequiredMixin, DetailView):
    """ Display task in detail(for logged in employee) """
    model = Task
    template_name = 'task/task_detail.html'
    context_object_name = "task_detail"


class ProjectTaskListView(LoginRequiredMixin, ListView):
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


class TaskList(LoginRequiredMixin, View):
    """Display list of tasks in selected project."""
    model = Project
    form_class = CreateTaskForm
    template_name = "task/project_tasklist.html"
    context_object_name = "tasklist"

    def get(self, request):
        try:
            project_id = self.request.GET.get('id', None)
            tasks = get_tasklist(project_id)
            data = {"task": tasks}
            return JsonResponse(data, safe=False)
        except Exception as e:
            logging.error(str(e))


class SearchTaskView(View):
    """for search task in all the tasks"""
    def get(self, request):
        try:
            project_id = self.request.GET.get('id', None)
            search = self.request.GET.get('search_here', None)
            task = search_task(project_id, search)
            data = {"task": task,
                    "error_message": "there is no task."}
            return render(request, 'task/search_list.html', data)
        except Exception as e:
            logging.error(str(e))


class TaskListBetweenDates(View):
    """ Display task in range of selected dates"""
    def get(self, request):
        try:
            project_id = self.request.GET.get('id', None)
            start_date = self.request.GET.get('start_date')
            end_date = self.request.GET.get('end_date')
            task = search_task_by_dates(project_id, start_date, end_date)
            data = {"task": task}
            return render(request, "task/search_list.html", data)
        except Exception as e:
            logging.error(str(e))
            return render(request, "task/search_list.html", data)

