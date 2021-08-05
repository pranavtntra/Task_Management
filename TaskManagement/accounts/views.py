from django.http.response import JsonResponse
from django.views.generic.list import ListView
from accounts.models import User
from accounts.forms import MyCustomSignupForm
from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.mail import send_mail
from django.db.models import Q
import json


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)


class UserDetails(ListView):
    """show the details of user"""
    try:
        model = User
        # context_object_name = 'userdetails'
        template_name = 'account/userdetails.html'
        paginate_by = 6
        ordering = ['username']
    except Exception as e:
        raise e


class SearchUser(View):
    """show the details of seached user"""
    try:
        def get(self, request, *args, **kwargs):
            search = self.request.GET.get('search_here')
            print(search)
            user_list = User.objects.filter(Q(username__icontains=search) |
                                            Q(email__icontains=search) |
                                            Q(first_name__icontains=search) |
                                            Q(designation__icontains=search))
            data = {"object_list": user_list}
            return render(request, "account/user_details_list.html", data)
    except Exception as e:
        raise e


class AddUser(View):
    """create the new custom user"""
    try:
        def get(self, request, *args, **kwargs):
            user_create_form = MyCustomSignupForm()
            return render(request, 'account/createuser.html', {'form': user_create_form})

        def post(self, request, *args, **kwargs):
            form = MyCustomSignupForm(request.POST)
            if form.is_valid():
                userdata = form.save(request)
                userdata.set_password(userdata.email)
                userdata.save()
                send_mail('Tntra: Task Management',
                            'Your name is Username and email address is Login Password', request.user.email, [userdata.email], fail_silently=False)
                return redirect('userdetails')
            return render(request, 'account/createuser.html', {'form': form})
    except Exception as e:
        raise e


class UserProfile(ListView):
    """show the profile of user"""
    try:
        model = User
        template_name = 'account/userprofile.html'
    except Exception as e:
        raise e
