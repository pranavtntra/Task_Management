from allauth.account.forms import SignupForm
from django import forms
from .models import User
from django.forms import ModelForm
from django.core import validators
import datetime
from phonenumber_field.formfields import PhoneNumberField
from django.utils.translation import gettext as _




class UserForm(SignupForm):
    contact = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': _('Phone')}),label=_("Phone number"), required=False)
    name = forms.CharField(label="Name", required=True, widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': "span11"}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email'}))

    class Meta:
        model = User


    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        if len(str(contact)) < 10:
            raise forms.ValidationError("Enter valid Contact details")
        return contact

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(str(username)) < 5:
            raise forms.ValidationError("Username should contain atleast 5 characters")
        return username

    def save(self, request):
        print(self.cleaned_data)
        user = super(UserForm, self).save(request)
        user.contact = self.cleaned_data['contact']
        user.email = self.cleaned_data['email']
        user.name = self.cleaned_data['name']
        user.save()
        return user

    


