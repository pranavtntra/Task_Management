from django import forms
from accounts.models import User
from project.models import Project
from djrichtextfield.models import RichTextField
import datetime


class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            "title",
            "description",
            "start_date",
            "end_date",
            "project_lead",
            "status",
        )
