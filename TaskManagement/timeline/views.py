from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import View,TemplateView
from project.models import Project, ProjectTeam

# Create your views here.

class Dashboard(LoginRequiredMixin,TemplateView):
    template_name = "dashboard.html"

    def get(self, request):
            data = [Project.objects.filter(status=1).count(),Project.objects.filter(status=2).count(),Project.objects.filter(status=3).count()]
            labels = ["In-Progress","To-Do","Done"]


            return render(request, 'timeline/piechart.html', {'labels': labels,
        'data': data,
            })


        

