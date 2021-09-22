from django import template
from task.models import Task
from project.models import Project, ProjectTeam, Role
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
def get_team_size(proj_id):
    return ProjectTeam.objects.filter(project__id=proj_id.id).count()


@register.simple_tag
def get_project_finish(proj_id):
    task = Task.objects.filter(project__id=proj_id.id).count()
    done_task = Task.objects.filter(project__id=proj_id.id, status="Done").count()
    finish_percentage = 0
    if task:
        finish_percentage = round(done_task*100/task, 2)
    return finish_percentage


@register.simple_tag
def get_role_count(proj_id):
    result = {}
    roles = Role.objects.all().values('name')
    for role in roles:
        result[role["name"]] = ProjectTeam.objects.filter(project__id=proj_id.id, role__name=role["name"]).count()
    return result
