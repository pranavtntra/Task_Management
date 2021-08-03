from project.models import Project
from task.models import Task
from django.views.generic import CreateView, ListView, View
from task.forms import CreateTaskForm, CreateSubTaskForm
from django.http import JsonResponse
import json
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
    """ Display list of tasks (for logged in user's list of tasks ) """
    model = Task
    template_name = "task/mytask_list.html"
    context_object_name = "tasklist"

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)


class ProjectTaskListView(ListView):
    """Display list of task Project wise"""
    model = Project
    form_class = CreateTaskForm
    template_name = "task/project_tasklist.html"
    context_object_name = "projectlist"

    def get_queryset(self):
        return Project.objects.all()


class TaskList(View):

    model = Project
    form_class = CreateTaskForm
    template_name = "task/project_tasklist.html"
    context_object_name = "tasklist"

    def get(self, request, *args, **kwargs):
        # import code; code.interact(local=dict(globals(), **locals()))
        project_id = self.request.GET.get('id', None)
        print(id)
        project_id = Project.objects.filter(id=project_id)
        if project_id.exists():
            # import code; code.interact(local=dict(globals(), **locals()))
            project = project_id.first()
            t = Task.objects.filter(project=project).values('title','assigned_to__first_name', 'status', 'priority', 'tasktype')
        tasks = json.dumps(list(t))
        print(tasks)
        data = {"task": tasks}
        return JsonResponse(data, safe=False)
