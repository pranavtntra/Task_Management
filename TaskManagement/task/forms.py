from django import forms
from task.models import Task


class CreateTaskForm(forms.ModelForm):
    """This form is for project manager to create a tasks and assign to employee."""
    class Meta:
        model = Task
        fields = (
            'title', 'description', 'project', 'assigned_to',
            'priority', 'status', 'start_date', 'end_date', 'tasktype'
        )
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if Task.objects.filter(title=title).exists():
            raise forms.ValidationError(u'title "%s" is already in use!' % title)
        return title


class CreateSubTaskForm(forms.ModelForm):
    """This form is for employee to create sub task"""
    class Meta:
        model = Task
        fields = (
            'parent_task', 'title', 'description', 'project',
            'priority', 'status', 'start_date', 'end_date', 'tasktype'
        )
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
        
    def clean_title(self):
        title = self.cleaned_data['title']
        if Task.objects.filter(title=title).exists():
            raise forms.ValidationError(u'title "%s" is already in use!' % title)
        return title
