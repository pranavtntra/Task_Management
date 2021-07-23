from django import forms
from allauth.account.forms import SignupForm
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField
# from .models import User


user_role = (
    ('Employee', 'Employee'),
)

alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only characters are allowed!')
# number = RegexValidator(r'^[0-9]*$', 'Enter valid contact number!')


class MySignupForm(SignupForm):
    firstName = forms.CharField(validators=[alpha], max_length=15, min_length=2)
    lastName = forms.CharField(validators=[alpha], max_length=15, min_length=2)
    # contact = forms.CharField(validators=[number], max_length=10, min_length=10)
    contact = PhoneNumberField()
    role = forms.ChoiceField(choices=user_role)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, request):
        user = super(MySignupForm, self).save(request)
        user.firstName = self.cleaned_data['firstName']
        user.lastName = self.cleaned_data['lastName']
        user.contact = self.cleaned_data['contact']
        user.role = self.cleaned_data['role']
        user.save()
        return user
