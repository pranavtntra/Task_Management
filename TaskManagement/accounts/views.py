from django.views.generic.list import ListView
from accounts.models import User
from accounts.forms import AddUserForm, UserUpdateForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from accounts.services import AccountManagement
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
import logging
import json
from accounts.models import IntermediateUserTech

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)


class UserList(LoginRequiredMixin, ListView):
    """show the details of user"""
    model = User
    template_name = 'account/userlist.html'
    paginate_by = 7
    ordering = ['-id']



class SearchUser(LoginRequiredMixin, View):
    """show the details of searched user"""

    def get(self, request, *args, **kwargs):
        try:
            search = self.request.GET.get('search')
            user_list = AccountManagement.get_user(self, search)
            paginator = Paginator(user_list, 7)
            page_number = request.GET.get('page')
            user_list = paginator.get_page(page_number)
            data = {"page_obj": user_list,
                    "error_message": 'No such data found'}
            return render(request, "account/user_details_list.html", data)
        except Exception as e:
            logging.error(str(e))
            data = {"page_obj": user_list}
            return render(request, "account/user_details_list.html", data)


class AddUser(LoginRequiredMixin, CreateView):
    """
    Administration can create user and set email-id as a password
    """
    model = User
    form_class = AddUserForm
    template_name = 'account/createuser.html'
    success_url = 'userlist'


    def post(self, request, *args, **kwargs):
        try:
            form = AddUserForm(request.POST)
            # import code;
            # code.interact(local=dict(globals(), **locals()))
            if form.is_valid():
                print("Inside")
                userdata = form.save()
                userdata.set_password(userdata.email)
                userdata.email_verified = True
                userdata.save()
                for tech, topic in zip(form.data.getlist('technologies', ''), form.data.getlist('topic', '')):
                    IntermediateUserTech.objects.filter(user_name_id=userdata, technologies_id=tech).update(topic=topic)
                userd = AccountManagement.set_email(self, userdata)
                return redirect('userlist')
            return render(request, 'account/createuser.html', {'form': form})
        except Exception as e:
            logging.error(str(e))
            return render(request, 'account/createuser.html', {'form': form})


class UserProfile(LoginRequiredMixin, ListView):
    """show the profile of user"""
    model = User
    template_name = 'account/userprofile.html'


class DeleteUser(LoginRequiredMixin, DeleteView):
    """delete the user from userlist"""
    model = User
    success_url = reverse_lazy('userlist')


class UpdateUser(LoginRequiredMixin, UpdateView):
    """User or administration can update the profile of user"""
    model = User
    form_class = UserUpdateForm
    template_name = 'account/update_user.html'
    success_url = reverse_lazy('dashboard')


class ChangePassword(PasswordChangeView):
    """User or administration can change the account password"""
    form_class = PasswordChangeForm
    success_url = reverse_lazy('dashboard')
    template_name = 'account/change_password.html'
