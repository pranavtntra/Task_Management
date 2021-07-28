from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from accounts.models import User
from django.urls import reverse_lazy


class UserDetails(ListView):
    model = User
    context_object_name = 'userdetails'
    template_name = 'userdetails.html'


class AddUser(CreateView):
    # form_class = MyCustomSignupForm
    redirect_authenticated_user = True
    model = User
    fields = ['email', 'username', 'first_name', 'last_name', 'contact', 'designation', 'password']
    success_url = reverse_lazy('dashboard')
    template_name = 'createuser.html'
