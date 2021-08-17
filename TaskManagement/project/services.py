from project.models import Project

def get_projects(user):
    if user.is_superuser:
        return Project.objects.all()
    else:
        proj_manager = Project.objects.filter(project_lead=user)
        employee = Project.objects.filter(projectteam__teammate=user)
        projects = proj_manager|employee
        return projects.distinct()
    