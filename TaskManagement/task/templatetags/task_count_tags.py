from django import template
from task.models import Task
from task.constants import STATUS

register = template.Library()


@register.simple_tag
def get_task_count(proj_id):
    return Task.objects.filter(project__id=proj_id.id).count()


@register.simple_tag
def get_task_status_count(proj_id):
    result = {}
    for status in STATUS:
        result[status[0]] = Task.objects.filter(project__id=proj_id.id, status=status[0]).count()
    return result

@register.simple_tag
def get_user_task_allocation(user_id):
    return Task.objects.filter(assigned_to = user_id).count()