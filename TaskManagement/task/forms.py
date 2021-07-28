from django import forms
from django.forms import widgets
from task.models import Task


class CreateTaskForm(forms.ModelForm):
    """This form is for project manager to create a tasks and assign to employee."""
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
        
        }
