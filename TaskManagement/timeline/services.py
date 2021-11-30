from project.models import Project, ProjectTeam
from accounts.models import User
from task.models import Task
from django.db.models import Q
import logging
from project.constants import STATUS


def get_dashboard(self, Dashboard):
    dashboard = {}
    try:
        dashboard = super(Dashboard, self).get_context_data()
        dashboard["total_user"] = User.objects.count()
        dashboard["project_manager"] = User.objects.filter(designation="Project Manager").count()
        dashboard["employee"] = User.objects.filter(designation="Employee").count()
        dashboard["total_projects"] = Project.objects.all().count()
        dashboard["active_projects"] = Project.objects.filter(status="1").count()
        proje_manager = Project.objects.filter(project_lead=self.request.user).count()
        employees = Project.objects.filter(projectteam__teammate=self.request.user).count()
        dashboard["user_total_project"] = proje_manager + employees
        project_manager = Project.objects.filter(project_lead=self.request.user, status=1).count()
        employee = Project.objects.filter(projectteam__teammate=self.request.user, status=1).count()
        dashboard["active"] = project_manager + employee
    except Exception as e:
        logging.error(str(e))
    return dashboard


def get_projects(user):
    if user.is_superuser:
        active_projects = Project.objects.filter(status=1)
        return active_projects
    else:
        project_manager = Project.objects.filter(project_lead=user, status=1)
        employee = Project.objects.filter(projectteam__teammate=user, status=1)
        active_projects = project_manager | employee
        return active_projects.distinct()


def get_status_count(obj, status):
    return obj.filter(status=status).count()


def get_piechart(user):
    projects = []
    if not user.is_superuser:
        project = Project.objects.filter(((Q(project_lead=user)|Q(projectteam__teammate=user)))).distinct()
    else:
        project = Project.objects.all()
    for status in STATUS:
        projects.append(get_status_count(project, status[0]))
    return projects


def get_employee_pdf(emp_name):
    emp_data = User.objects.get(username=emp_name)
    return emp_data


def get_employee_project_pdf(emp_data):
    project_list = set(Project.objects.filter(Q(project_lead=emp_data) | Q(projectteam__teammate=emp_data)))
    proj_list = []
    for i in project_list:
        task_count = Task.objects.filter(assigned_to=emp_data, project=i).count()

        if str(i.project_lead) == emp_data.username:
            lead = 'Yes'
        else:
            lead = 'No'
        params = {
            'name': i.title,
            'start_date': i.start_date,
            'end_date': i.end_date,
            'get_status_display': i.get_status_display,
            'lead': lead,
            'task_count': task_count
        }
        proj_list.append(params)
    return proj_list


def get_project_status(project_name):
    project_data = Project.objects.get(title=project_name)
    task_list = Task.objects.filter(project=project_data).count()
    project_team = ProjectTeam.objects.filter(project=project_data)
    context = {
        'project_data': project_data,
        'task_list': task_list,
        'project_team': project_team
    }
    return context


def get_complete_project_report():
    complete_project = Project.objects.filter(status=3)
    context = {
        'complete_project': complete_project
    }
    return context


def get_active_project_report():
    active_project = Project.objects.filter(status=1)
    context = {
        'active_project': active_project
    }
    return context


def get_active_project_pdf(project_name):
    project_data = Project.objects.get(title=project_name)
    task_list = Task.objects.filter(project=project_data).count()
    project_team = ProjectTeam.objects.filter(project=project_data)
    done_task = Task.objects.filter(project=project_data, status='Done').count()

    finish_percentage = 0
    if task_list:
        finish_percentage = round(done_task * 100 / task_list, 2)

    context = {
        'project_data': project_data,
        'project_team': project_team,
        'task_list': task_list,
        'done_task': done_task,
        'finish_percentage': finish_percentage

    }
    return context


    