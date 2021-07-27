from django.contrib import admin
from project.models import Project, ProjectTeam, Role
# Register your models here.

admin.site.register(Project)
admin.site.register(Role)
admin.site.register(ProjectTeam)