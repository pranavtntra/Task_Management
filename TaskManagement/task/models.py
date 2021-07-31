from django.db import models
from project.models import Project
from accounts.models import User
from djrichtextfield.models import RichTextField
from django.urls import reverse
from task.constants import PRIORITY, STATUS, TASKTYPES, SPRINT_STATUS
# Create your models here.

PRIORITY = PRIORITY
STATUS = STATUS
TASKTYPES = TASKTYPES
SPRINT_STATUS = SPRINT_STATUS


class Task(models.Model):
    """Task is a model of task where number of tasks will be created for particular project"""
    title = models.CharField(max_length=50, blank=True, null=True)
    description = RichTextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='employee', on_delete=models.CASCADE)
    priority = models.CharField(max_length=30, choices=PRIORITY)
    status = models.CharField(max_length=30, choices=STATUS)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    tasktype = models.CharField(max_length=30, choices=TASKTYPES)
    parent_task = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("dashboard")


class Sprint(models.Model):
    """A sprint model is a group of related tasks combined together has to be completed in specific time. """
    name = models.CharField(max_length=50, blank=True, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=30, choices=SPRINT_STATUS)
