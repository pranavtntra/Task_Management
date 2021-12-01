from django.db import models
from accounts.models import User
from djrichtextfield.models import RichTextField
from django.urls import reverse
from project.constants import STATUS

# Create your models here.


class Project(models.Model):
    """A project model is for creating a multiple projects"""

    title = models.CharField(max_length=50, blank=True, null=True, unique=True)
    description = RichTextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=30, choices=STATUS)
    project_lead = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("listproject")


class Role(models.Model):
    """A role model is to specify role of employee's in particular project"""

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ProjectTeam(models.Model):
    """A project-team is creating team for particular project"""

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    teammate = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
