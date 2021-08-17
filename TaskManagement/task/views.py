from project.models import Project
from task.models import Task
from django.views.generic import CreateView, ListView, View, DetailView
from task.forms import CreateTaskForm, CreateSubTaskForm
from django.http import JsonResponse
import json
from django.shortcuts import redirect, render
from django.db.models import Q

# Create your views here.


class CreateTaskView(CreateView):
    """ Display form where pm can create task and assign to employee."""
    model = Task
    form_class = CreateTaskForm
    template_name = 'task/add_task.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(CreateTaskView, self).form_valid(form)


class CreateSubTaskView(CreateView):
    """ Display form where employee can create subtask."""
    model = Task
    form_class = CreateSubTaskForm
    template_name = 'task/add_subtask.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.assigned_to = self.request.user
        return super(CreateSubTaskView, self).form_valid(form)


class TaskListView(ListView):
    """ Display list of tasks (for logged in employee's list of tasks ) """
    model = Task
    template_name = "task/mytask_list.html"
    context_object_name = "tasklist"

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)


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
        return Project.objects.all()


class TaskList(View):
    """Display list of tasks in selected project."""
    model = Project
    form_class = CreateTaskForm
    template_name = "task/project_tasklist.html"
    context_object_name = "tasklist"

    def get(self, request):
        try:
            project_id = self.request.GET.get('id', None)
            print(id)
            project_id = Project.objects.filter(id=project_id)
            if project_id.exists():
                # import code; code.interact(local=dict(globals(), **locals()))
                project = project_id.first()
                t = Task.objects.filter(project=project).values('title', 'assigned_to__first_name', 'status', 'priority', 'tasktype')
            tasks = json.dumps(list(t))
            print(tasks)
            data = {"task": tasks}
            return JsonResponse(data, safe=False)
        except:
            return JsonResponse('dashboard.html')

    


class SearchTaskView(View):
    """for search task in all the tasks"""
    def get(self, request):
        try:
            search = self.request.GET.get('search_here', None)
            print(search)
            task = Task.objects.filter(Q(title__icontains=search) |
                                    Q(assigned_to__first_name__icontains=search) |
                                    Q(priority__icontains=search) |
                                    Q(tasktype__icontains=search))
            print(task)
            data = {"task": task}
            return render(request, 'task/search_list.html', data)
        except:
            return render('dashboard.html')


class TaskListBetweenDates(View):
    """ Display task in range of selected dates"""
    def get(self, request):
        try:
            start_date = self.request.GET.get('start_date')
            end_date = self.request.GET.get('end_date')
            print(start_date, end_date)
            task = Task.objects.filter(start_date__icontains=start_date)
            print(task)
            data = {"task": task}
            return render(request, "task/project_tasklist.html", data)
        except:
            return render('dashboard.html')
