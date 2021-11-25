from accounts.models import User
from django import forms
from task.models import Task
from project.models import Project
from task.constants import STATUS
import logging


class CreateTaskForm(forms.ModelForm):
    """This form is for project manager to create a tasks and assign to employee."""
    status = forms.TypedChoiceField(choices=STATUS, initial='To-Do')

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

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)
        if self.request.user.is_superuser:
            self.fields["project"].queryset = Project.objects.all()
        else:
            self.fields["project"].queryset = Project.objects.filter(
                project_lead=self.request.user)

        self.fields["assigned_to"].queryset = User.objects.filter(
            designation="Employee")


class CreateSubTaskForm(forms.ModelForm):
    """This form is for employee to create sub task"""
    status = forms.TypedChoiceField(choices=STATUS, initial='To-Do')

    class Meta:
        model = Task
        fields = (
            'project', 'parent_task', 'title', 'description',
            'priority', 'status', 'start_date', 'end_date', 'tasktype'
        )
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(CreateSubTaskForm, self).__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.all()
        self.fields['parent_task'].queryset = Task.objects.none()
        if 'project' in self.data:
            try:
                project_id = self.data.get('project')
                parent_t = Task.objects.filter(project=project_id)
                self.fields['parent_task'].queryset = parent_t.filter(
                    assigned_to=self.request.user)
            except (ValueError, TypeError):
                logging.error(ValueError, TypeError)

    def clean_title(self):
        title = self.cleaned_data['title']
        if Task.objects.filter(title=title).exists():
            raise forms.ValidationError(
                u'title "%s" is already in use!' % title)
        return title


class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'status')
