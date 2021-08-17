from django.views.generic.list import ListView
from accounts.models import User
from accounts.forms import AddUserForm, UserUpdateForm
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from accounts.services import AccountManagement
from accounts.constants import SIGNUP_MESSAGES, SIGNUP_SUBJECT
import logging
import json

SUBJECT = SIGNUP_SUBJECT
MESSAGES = SIGNUP_MESSAGES


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)


class UserDetails(ListView):
    """show the details of user"""
    model = User
    template_name = 'account/userdetails.html'
    paginate_by = 6
    ordering = ['username']


class SearchUser(View):
    """show the details of searched user"""
    def get(self, request, *args, **kwargs):
        try:
            search = self.request.GET.get('search_here')
            user_list = AccountManagement.get_user(self, search)
            data = {"object_list": user_list}
            return render(request, "account/user_details_list.html", data)
        except Exception as e:
            logging.error(str(e))
            data = {"object_list": user_list}
            return render(request, "account/user_details_list.html", data)


class AddUser(CreateView):
    """
    Administration can create user and set email-id as a password
    """
    model = User
    form_class = AddUserForm
    template_name = 'account/createuser.html'
    success_url = 'userdetails'

    def post(self, request, *args, **kwargs):
        try:
            form = AddUserForm(request.POST)
            if form.is_valid():
                userdata = form.save(request)
                userdata.set_password(userdata.email)
                userdata.save()
                send_mail(SUBJECT, MESSAGES, request.user.email, [userdata.email], fail_silently=False)
                return redirect('userdetails')
            return render(request, 'account/createuser.html', {'form': form})
        except Exception as e:
            logging.error(str(e))
            return render(request, 'account/createuser.html', {'form': form})


class UserProfile(ListView):
    """show the profile of user"""
    model = User
    template_name = 'account/userprofile.html'


class DeleteUser(DeleteView):
    """delete the user from userlist"""
    model = User
    success_url = reverse_lazy('userdetails')


class UpdateUser(UpdateView):
    """User or administration can update the profile of user"""
    model = User
    form_class = UserUpdateForm
    template_name = 'account/update_user.html'
    success_url = reverse_lazy('dashboard')
