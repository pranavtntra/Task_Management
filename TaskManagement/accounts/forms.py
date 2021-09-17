from accounts.models import User
from django import forms
from allauth.account.forms import SignupForm
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.forms import PasswordChangeForm
from accounts.constants import DESIGNATION

Designation = DESIGNATION


class MyCustomSignupForm(SignupForm):
    """ This form is All auth User registration """
    email = forms.EmailField(
        required=True,
        max_length=122,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your email name"}
        ),
    )
    username = forms.CharField(
        max_length=122,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your username"}
        ),
    )
    first_name = forms.CharField(
        max_length=122,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your first name"}
        ),
    )
    last_name = forms.CharField(
        max_length=122,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your last name"}
        ),
    )
    contact = PhoneNumberField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your contact number"}
        )
    )
    designation = forms.ChoiceField(choices=Designation)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.contact = self.cleaned_data["contact"]
        user.designation = self.cleaned_data["designation"]
        user.save()
        return user


class AddUserForm(forms.ModelForm):
    """ This form for create new user by administration."""
    email = forms.EmailField(
        required=True,
        max_length=122,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your email name"}
        ),
    )
    username = forms.CharField(
        max_length=122,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your username"}
        ),
    )
    first_name = forms.CharField(
        max_length=122,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your first name"}
        ),
    )
    last_name = forms.CharField(
        max_length=122,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your last name"}
        ),
    )
    contact = PhoneNumberField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your contact number"}
        )
    )
    designation = forms.ChoiceField(choices=Designation)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'contact', 'designation')


class UserUpdateForm(forms.ModelForm):
    """
    this is update form administartion can update user details and user can also update profile
    """
    username = forms.CharField(
        max_length=122,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your username"}
        ),
    )
    first_name = forms.CharField(
        max_length=122,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your first name"}
        ),
    )
    last_name = forms.CharField(
        max_length=122,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your last name"}
        ),
    )
    contact = PhoneNumberField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your contact number"}
        )
    )
    email = forms.EmailField(
        required=True,
        max_length=122,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your email name"}
        ),
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'contact', 'email')


class PasswordChangeForm(PasswordChangeForm):
        error_css_class = 'has-error'
        error_messages = {'password_incorrect':
                  "The old password is not correct. Please try again."}
        old_password = forms.CharField(required=True, label='Old Password',
                      widget=forms.PasswordInput(attrs={
                        'class': 'form-control'}),
                      error_messages={
                        'required': 'The password can not be empty'})

        new_password1 = forms.CharField(required=True, label='New Password',
                      widget=forms.PasswordInput(attrs={
                        'class': 'form-control'}),
                      error_messages={
                        'required': 'The password can not be empty'})
        new_password2 = forms.CharField(required=True, label='New Password (Repeat)',
                      widget=forms.PasswordInput(attrs={
                        'class': 'form-control'}),
                      error_messages={
                        'required': 'The password can not be empty'})
