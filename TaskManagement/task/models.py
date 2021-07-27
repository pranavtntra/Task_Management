from django.db import models
from project.models import Project
from accounts.models import User
from djrichtextfield.models import RichTextField
# Create your models here.

PRIORITY = (
        ('Lower', 'Lower'),
        ('Medium', 'Medium'),
        ('High', 'High'),
)
STATUS = (
    ('1', 'To-do'),
    ('2', 'In-progress'),
    ('3', 'Done'),
    ('4', 'Declined'),
    ('5', 'Ready For Testing'),
    ('6', 'Code Review'),
    ('7', 'Testing in-progress')
)

TASKTYPES = (
    ('1', 'Bug'),
    ('2', 'Improvement'),
    ('3', 'New Feature'),
    ('4', 'Story'),
    ('5', 'Task'),
    ('6', 'Epic')
)

SPRINT_STATUS = (
    ('1', 'Planning'),
    ('2', 'Active'),
    ('3', 'Accepted'),
    ('4', 'Closed')
)


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


class Sprint(models.Model):
    """A sprint model is a group of related tasks combined together has to be completed in specific time. """
    name = models.CharField(max_length=50, blank=True, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=30, choices=SPRINT_STATUS)


#class FileAttachment(models.Model):
#    file_name = models.CharField(max_length=60, blank=True, null=True)
