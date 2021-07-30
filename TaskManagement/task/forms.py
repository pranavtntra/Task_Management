from django import forms
from task.models import Task


class CreateTaskForm(forms.ModelForm):
    """This form is for project manager to create a tasks and assign to employee."""
    class Meta:
        model = Task
        fields = (
            'title', 'description', 'project', 'created_by', 'assigned_to',
            'priority', 'status', 'start_date', 'end_date', 'tasktype'
        )


class CreateSubTaskForm(forms.ModelForm):
    """This form is for project manager to create a tasks and assign to employee."""
    class Meta:
        model = Task
        fields = (
            'parent_task', 'title', 'description', 'project',
            'priority', 'status', 'start_date', 'end_date', 'tasktype'
        )
