from django import forms
from accounts.models import User
from project.models import Project, ProjectTeam
from djrichtextfield.models import RichTextField
import datetime
from django.core.exceptions import ValidationError


class CreateProjectForm(forms.ModelForm):
    title = forms.CharField()
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'placeholder': 'YYYY-MM-DD', 'required': 'required','id':'start'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'placeholder': 'YYYY-MM-DD', 'required': 'required','id':'end'}))
    

    
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


    def clean_title(self):
        title = self.cleaned_data['title']
        if Project.objects.filter(title=title).exists():
            raise forms.ValidationError("title already exists.")
        return title
    
    def clean(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        if start_date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        if end_date <= start_date:
            raise forms.ValidationError("End date should be greater than start date.")
        return self.cleaned_data

class AddMemberForm(forms.ModelForm):
    class Meta:
        model = ProjectTeam
        fields =('teammate','role')


    
        






       
        

        
        
        


        

