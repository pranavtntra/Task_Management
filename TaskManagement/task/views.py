from project.models import Project
from accounts.models import User
from task.models import Task
from django.views.generic import CreateView, ListView
from task.forms import CreateTaskForm, CreateSubTaskForm
from django.http import JsonResponse
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
    template_name = "task/task_list.html"
    context_object_name = "tasklist"
 
    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)
        

class ProjectTaskListView(ListView):
    """Display list of task Project wise"""
    model = Project
    template_name = "task/project_tasklist.html"
    context_object_name = "projectlist"
    
    #def get_queryset(self):
    #    
    #    
    #    id = self.request.GET.get("id")
    #    print(self.request.GET.get("project"))
    #    print(id)
    #    print(self.request.GET)
    #    #if project == "":
    #    #    Task.objects.none()
    #    return Project.objects.filter(project_lead=id)
    
    def get_context_data(self, **kwargs):
        #import code; code.interact(local=dict(globals(), **locals()))
        project_list = []
        context = super(ProjectTaskListView, self).get_context_data(**kwargs)
        project_list = Project.objects.all()
        context['project'] = [project.title for project in project_list]
        return context
