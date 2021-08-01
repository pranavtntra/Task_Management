from django.views.generic.list import ListView
from accounts.models import User
from accounts.forms import MyCustomSignupForm
from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.mail import send_mail


class UserDetails(ListView):
    """show the details of user"""
    try:
        model = User
        context_object_name = 'userdetails'
        template_name = 'userdetails.html'
        paginate_by = 6
    except Exception as e:
        raise e


class AddUser(View):
    """create the new custom user"""
    try:
        def get(self, request, *args, **kwargs):
            user_create_form = MyCustomSignupForm()
            return render(request, 'createuser.html', {'form': user_create_form})

        def post(self, request, *args, **kwargs):
            form = MyCustomSignupForm(request.POST)
            if form.is_valid():
                userdata = form.save(request)
                userdata.set_password(userdata.email)
                userdata.save()
                send_mail('Tntra: Task Management',
                            'Your name is Username and email address is Login Password', request.user.email, [userdata.email], fail_silently=False)
                return redirect('userdetails')
            return render(request, 'createuser.html', {'form': form})
    except Exception as e:
        raise e


class UserProfile(ListView):
    """show the profile of user"""
    try:
        model = User
        template_name = 'userprofile.html'
    except Exception as e:
        raise e
