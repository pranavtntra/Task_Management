from django import forms
from allauth.account.forms import SignupForm
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField

user_role = (
    ('Employee', 'Employee'),
    ('Project Manager', 'Project Manager'),
)
alpha = RegexValidator(r'^[a-zA-Z]*$', 'Numbers are not allowed in name!')
# number = RegexValidator(r'^[0-9]*$', 'Enter valid contact number!')


class MySignupForm(SignupForm):
    firstName = forms.CharField(validators=[alpha], max_length=15,
                                min_length=2)
    lastName = forms.CharField(validators=[alpha], max_length=15, min_length=2)
    contact = PhoneNumberField()
    role = forms.ChoiceField(choices=user_role)

    def __init__(self, *args, **kwargs):
        super(MySignupForm, self).__init__(*args, **kwargs)

    def save(self, request):
        user = super(MySignupForm, self).save(request)
        user.firstName = self.cleaned_data['firstName']
        user.lastName = self.cleaned_data['lastName']
        user.contact = self.cleaned_data['contact']
        user.role = self.cleaned_data['role']
        user.save()
        return user
