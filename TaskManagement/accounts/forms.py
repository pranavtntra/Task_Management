from django import forms
from allauth.account.forms import SignupForm
from phonenumber_field.formfields import PhoneNumberField


Role = (
        ('Project Manager', 'Project Manager'),
        ('Employee', 'Employee'),
    )

class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=122,)
    last_name = forms.CharField(max_length=122)
    contact = PhoneNumberField()
    role = forms.ChoiceField(choices=Role)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_contact(self):
        contact = self.cleaned_data.get("contact")
        z = contact.parse(contact, "IN")
        if not contact.is_valid_number(z):
            raise forms.ValidationError("Number not in IN format")
        return contact

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.contact = self.cleaned_data['contact']
        user.role = self.cleaned_data['role']
        print(user.first_name)
        user.save()
        return user