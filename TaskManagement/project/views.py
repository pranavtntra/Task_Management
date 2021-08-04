from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views.generic import View, CreateView, ListView
from project.forms import CreateProjectForm
from project.models import Project
from django.urls import reverse_lazy


class CreateProjectView(CreateView):
    model = Project
    template_name = "project/create_project.html"
    form_class = CreateProjectForm
    # succes_url = reverse_lazy('list-project')


class ListProjectView(ListView):
    model = Project
    template_name = "project/list_project.html"
    context_object_name = "projectlist"

    def get_queryset(self):
        return Project.objects.all()
