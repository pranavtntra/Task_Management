from django.views.generic.list import ListView
from project.models import Project
from django.shortcuts import render
from django.views.generic import TemplateView
from .services import get_projects, get_dashboard, get_piechart
from django.contrib.auth.mixins import LoginRequiredMixin
from .constants import PIECHART_LABELS

import logging

# Create your views here.


class Dashboard(LoginRequiredMixin, TemplateView):
    """
    Show the details on dashboard
    """
    template_name = "dashboard.html"

    # def get_context_data(self, *args, **kwargs):
    #     return get_dashboard(self, Dashboard)

    def get(self, request):
        data = get_piechart(self.request.user)
        labels = PIECHART_LABELS
        dashboard_data = get_dashboard(self, Dashboard)
        return render(request, 'dashboard.html', {'labels': labels, 'data': data, 'dashboard_data': dashboard_data})


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
