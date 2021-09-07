from task.models import Task
from project.models import Project
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.db.models import Q


def get_tasklist(project_id):
    project_id = Project.objects.filter(id=project_id)
    if project_id.exists():
        project = project_id.first()
        task_list = Task.objects.filter(project=project).values('title', 'assigned_to__first_name', 'status', 'priority', 'tasktype', 'start_date__date', 'end_date__date')
        tasks = json.dumps(list(task_list), cls=DjangoJSONEncoder)
    return tasks


def search_task(project_id, search):
    project = Project.objects.filter(id=project_id).last()
    task_list = Task.objects.filter(project=project)
    task = task_list.filter(Q(title__icontains=search) |
                            Q(assigned_to__first_name__icontains=search) |
                            Q(priority__icontains=search) |
                            Q(tasktype__icontains=search)).order_by('-id')
    return task


def search_task_by_dates(project_id, start_date, end_date):
    project = Project.objects.filter(id=project_id).last()
    task_list = Task.objects.filter(project=project)
    task = task_list.filter(Q(start_date__gte=start_date) & Q(end_date__lte=end_date))
    return task
