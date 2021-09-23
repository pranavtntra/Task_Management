from project.models import Project
from accounts.models import User
import logging


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
