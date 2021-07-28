from accounts.models import Designation
from django import forms
from allauth.account.forms import SignupForm
from phonenumber_field.formfields import PhoneNumberField

Designation = (
        ('Project Manager', 'Project Manager'),
        ('Employee', 'Employee'),
    )


class MyCustomSignupForm(SignupForm):
    email = forms.EmailField(required=True, max_length=122, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your email name'}))
    username= forms.CharField(max_length=122, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your username'}))
    first_name = forms.CharField(max_length=122, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your first name'}))
    last_name = forms.CharField(max_length=122, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your last name'}))
    contact = PhoneNumberField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your contact number'}))
    designation = forms.ChoiceField(choices=Designation)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.contact = self.cleaned_data['contact']
        user.designation = self.cleaned_data['designation']
        user.save()
        return user
