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



class CreateProjectView(LoginRequiredMixin,CreateView):
    model = Project
    template_name = "project/create_project.html"
    form_class = CreateProjectForm


    def get_form(self, *args, **kwargs):
        try:
            form = super(CreateProjectView, self).get_form(*args, **kwargs)
            form.fields['project_lead'].queryset = User.objects.filter(is_superuser=False)
            return form
        except Exception as error:
            raise error



class ListProjectView(LoginRequiredMixin,ListView):
    model = Project
    template_name = "project/list_project.html"
    context_object_name = "projectlist"

    def get_queryset(self):
        try:
            return get_projects(self.request.user) 
        except Exception as error:
            raise error


class SearchProjectView(View):
    
        def get(self, request, *args, **kwargs):
            try:
                search = self.request.GET.get('search')
                projectlist = get_projects(self.request.user).filter(Q(title__icontains=search) | Q(project_lead__username__icontains=search))
                proj_list = {"search_projectlist": projectlist} 
                return render(request, "project/listproject.html", proj_list)
            except Exception as error:
                raise error

class SortProjectView(View):
    def get(self, request):
        try:
            selected = self.request.GET.get('sort')
            data = {
                "T+" : get_projects(self.request.user).order_by('title'),
                "T-" : get_projects(self.request.user).order_by('-title'),
                "S+" : get_projects(self.request.user).order_by('start_date'),
                "S-" : get_projects(self.request.user).order_by('-start_date'),
                "E+" : get_projects(self.request.user).order_by('end_date'),
                "E-" : get_projects(self.request.user).order_by('-end_date')

                }
      
            projectlist = data[selected]
            proj_list = {"search_projectlist": projectlist} 
            return render(request, "project/listproject.html", proj_list)
        except Exception as error:
            raise error

class AddEmployeeView(LoginRequiredMixin,CreateView):
    pass


            
        
           

            

