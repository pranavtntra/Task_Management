from django import template
from task.models import Task
from project.models import ProjectTeam, Role, Project

register = template.Library()


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

@register.simple_tag
def get_project_count(user_id):
    """ for count of project allocation to project manager and employee. """
    task = len(set([task.project for task in Task.objects.filter(assigned_to=user_id)]))
    return Project.objects.filter(project_lead=user_id).count() or task

@register.simple_tag
def get_project_title(user_id):
    """ for display a list of projects which are allocated to project manager and employee
        tasks : to get project list of employee,
        projects : to get project list of employee,
        we used update method to join both list and for get title
    """
    tasks = set([task.project for task in Task.objects.filter(assigned_to=user_id)])
    projects = Project.objects.filter(project_lead=user_id)
    tasks.update(set(projects))
    data = ''
    for p_title in tasks:
        data += p_title.title +","
    return data[:-1]
