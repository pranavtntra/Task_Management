from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views.generic import View, CreateView, ListView
from project.forms import CreateProjectForm
from project.models import Project, ProjectTeam
from django.urls import reverse_lazy
from accounts.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
import json
from .services import get_projects
import logging
from .constants import SORTER




class CreateProjectView(LoginRequiredMixin,CreateView):
    model = Project
    template_name = "project/create_project.html"
    form_class = CreateProjectForm


    def get_form(self, *args, **kwargs):
            form = super(CreateProjectView, self).get_form(*args, **kwargs)
            try:
                form.fields['project_lead'].queryset = User.objects.filter(is_superuser=False)
                return form
            except Exception as error:
                logging.error(str(e))
                return form



class ListProjectView(LoginRequiredMixin,ListView):
    model = Project
    template_name = "project/list_project.html"
    context_object_name = "projectlist"

    def get_queryset(self):
        try:
            return get_projects(self.request.user) 
        except Exception as error:
            logging.error(str(e))


class SearchProjectView(View):

    def get(self, request, *args, **kwargs):
        search = self.request.GET.get('search')
        projectlist = get_projects(self.request.user)
        try:
            projectlist = projectlist.filter(Q(title__icontains=search) | Q(project_lead__username__icontains=search))
            proj_list = {
                "search_projectlist": projectlist,
                "error_message": 'No such data found'
            } 
            return render(request, "project/listproject.html", proj_list)
        except Exception as e:
            logging.error(str(e))
            proj_list = {"search_projectlist": projectlist} 
            return render(request, "project/listproject.html", proj_list)

class SortProjectView(View):

    def get(self, request):
            selected = self.request.GET.get('sort')
            projectlist =  get_projects(self.request.user)    
            try:
                projectlist = projectlist.order_by(SORTER[selected])
                proj_list = {"search_projectlist": projectlist} 
                return render(request, "project/listproject.html", proj_list)
            except Exception as error:
                logging.error(str(e))
                proj_list = {"search_projectlist": projectlist} 
                return render(request, "project/listproject.html", proj_list)
            

class AddEmployeeView(LoginRequiredMixin,CreateView):
    pass


            
        
           

            

