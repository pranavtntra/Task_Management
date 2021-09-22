from logging import exception
from django import forms
import django
from django.views.generic.base import View
from django.views.generic.list import ListView
from accounts.models import User
from project.models import Project
from task.models import Task
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView
from .services import get_projects, get_dashboard
import logging

# Create your views here.


class Dashboard(TemplateView):
    """
    Show the details on dashboard
    """
    template_name = "dashboard.html"

    def get_context_data(self, *args, **kwargs):
        return get_dashboard(self, Dashboard)


class ActiveProjects(ListView):
    """
    show the total active projects for admin and user for his active projects
    """
    model = Project
    template_name = "active_projects.html"
    context_object_name = "active_projects"

    def get_queryset(self):
        try:
            return get_projects(self.request.user)
        except Exception as e:
            logging.error(str(e))