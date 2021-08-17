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
        form = super(CreateProjectView, self).get_form(*args, **kwargs)
        form.fields['project_lead'].queryset = User.objects.filter(is_superuser=False)
        return form



class ListProjectView(LoginRequiredMixin,ListView):
    model = Project
    template_name = "project/list_project.html"
    context_object_name = "projectlist"

    def get_queryset(self):
        return get_projects(self.request.user) 


class SearchProjectView(View):
    
        def get(self, request, *args, **kwargs):
            search = self.request.GET.get('chuzza')
            # import code; code.interact(local=dict(globals(), **locals()))
            # project_searchlist = serializers.serialize('json',Project.objects.filter(Q(title__icontains=search) | Q(project_lead__icontains=search)))
            projectlist = get_projects(self.request.user).filter(Q(title__icontains=search) | Q(project_lead__username__icontains=search))
            babu = {"search_projectlist": projectlist} 
            
            # print(len(babu["search_projectlist"]))
            return render(request, "project/listproject.html", babu)

class SortProjectView(View):
    def get(self, request):
        # print("hey")
        selected = self.request.GET.get('sort')
        data = {
             "T+" : get_projects(self.request.user).order_by('title'),
             "T-" : get_projects(self.request.user).order_by('-title'),
             "S+" : get_projects(self.request.user).order_by('start_date'),
             "S-" : get_projects(self.request.user).order_by('-start_date'),
             "E+" : get_projects(self.request.user).order_by('end_date'),
             "E-" : get_projects(self.request.user).order_by('-end_date')

        }
        # if selected == "T-":
        #     projectlist = get_projects(self.request.user).order_by('title')
        projectlist = data[selected]
        babu = {"search_projectlist": projectlist} 
        return render(request, "project/listproject.html", babu)

class AddEmployeeView(LoginRequiredMixin,CreateView):
    pass


            
        
           

            

