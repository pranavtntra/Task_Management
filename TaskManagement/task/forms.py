from accounts.models import User
from django import forms
from task.models import Task
from project.models import Project,ProjectTeam
from task.constants import STATUS


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
            self.fields["project"].queryset = Project.objects.filter(project_lead = self.request.user)

        self.fields["assigned_to"].queryset = User.objects.filter(designation="Employee")

        #self.fields['assigned_to'].queryset = ProjectTeam.objects.none()
        #if 'project' in self.data:
        #    try:
        #        project_id = int(self.data.get('project'))
        #        assign = Project.objects.filter(id = project_id)
        #        self.fields['assigned_to'].queryset =  ProjectTeam.objects.filter(id=assign.teammate.id)
        #    except (ValueError, TypeError):
        #        pass
    
    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if Task.objects.filter(title=title).exists():
    #         raise forms.ValidationError(u'title "%s" is already in use!' % title)
    #     return title


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

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(CreateSubTaskForm, self).__init__(*args, **kwargs)
        #import code; code.interact(local=dict(globals(), **locals()))
        self.fields["parent_task"].queryset = Task.objects.filter(assigned_to=self.request.user)
        self.fields['project'].queryset = Task.objects.none()

        if 'parent_task' in self.data:
            try:
                task_id = self.data.get('parent_task')
                task = Task.objects.get(id=task_id)
                self.fields['project'].queryset = Project.objects.filter(id=task.project.id) if task else Project.objects.none()
            except (ValueError, TypeError):
                pass

    def clean_title(self):
        title = self.cleaned_data['title']
        if Task.objects.filter(title=title).exists():
            raise forms.ValidationError(u'title "%s" is already in use!' % title)
        return title
