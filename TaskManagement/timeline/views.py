from django.db.models import Q
from django.views.generic.list import ListView
from accounts.models import User
from project.models import Project, ProjectTeam
from task.models import Task
from django.shortcuts import render
from django.views.generic import TemplateView, View
from .services import get_projects, get_dashboard, get_piechart, get_employee_project_pdf,\
                        get_employee_pdf, get_active_project_pdf, get_active_project_report,\
                        get_complete_project_report, get_project_status
from django.contrib.auth.mixins import LoginRequiredMixin
from .constants import PIECHART_LABELS
from .render import Render

import logging

# Create your views here.


class Dashboard(LoginRequiredMixin, TemplateView):
    """
    Show the details on dashboard
    """
    template_name = "dashboard.html"

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


class Employee_report(ListView):
    """
    Select the employee for employee report
    """
    model = User
    template_name = "timeline/employee_report.html"
    context_object_name = "employee_list"


class EmployeePdf(View):
    """
    Generate the employee report
    """
    def get(self, request):
        emp_name = request.GET['emp_list']
        try:
            emp_data = get_employee_pdf(emp_name)
            proj_list = get_employee_project_pdf(emp_data)
            return Render.render('timeline/employee_pdf.html', {'proj_list': proj_list,
                                                                'emp_data': emp_data})
        except Exception as e:
            logging.error(str(e))


class ProjectStatusReport(ListView):
    """
    Select the Project for Project status report
    """
    model = Project
    template_name = "timeline/project_status_report.html"
    context_object_name = "project_status"


class ProjectStatusPdf(View):
    """
    Generate the Project Status report for selected project
    """
    def get(self, request):
        project_name = request.GET['project_list']
        try:
            context = get_project_status(project_name)
            return Render.render('timeline/project_status_pdf.html', context)
        except Exception as e:
            logging.error(str(e))


class CompleteProjectReport(View):
    """
    List of completed project where status are closed or 3
    """
    def get(self, request):
        try:
            context = get_complete_project_report()
            return render(request, 'timeline/complete_project_report.html', context)
        except Exception as e:
            logging.error(str(e))


class CompleteProjectPdf(View):
    """
    Generate the PDF for selected complete project.
    """
    def get(self, request):
        project_name = request.GET['complete_project']
        try:
            context = get_project_status(project_name)
            return Render.render('timeline/complete_project_pdf.html', context)
        except Exception as e:
            logging.error(str(e))


class ActiveProjectReport(View):
    """
    List of Active project where status are Under Process or 1
    """
    def get(self, request):
        try:
            context = get_active_project_report()
            return render(request, 'timeline/active_project_report.html', context)
        except Exception as e:
            logging.error(str(e))


class ActiveProjectPdf(View):
    """
    Generate the PDF for selected Active project.
    """
    def get(self, request):
        project_name = request.GET['active_project']
        try:
            context = get_active_project_pdf(project_name)
            return Render.render('timeline/active_project_pdf.html', context)
        except Exception as e:
            logging.error(str(e))


class SprintReport(ListView):
    model = Project
    template_name = "timeline/sprint_report.html"
    context_object_name = "sprint"
