from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import View,TemplateView
from project.models import Project, ProjectTeam
from .constants import PIECHART_LABELS

# Create your views here.

class Dashboard(LoginRequiredMixin,TemplateView):
    template_name = "dashboard.html"

    def get(self, request):
            data = [Project.objects.filter(status=1).count(),Project.objects.filter(status=2).count(),Project.objects.filter(status=3).count()]
            labels = PIECHART_LABELS


            return render(request, 'timeline/piechart.html', {'labels': labels,
        'data': data,
            })

# from django.db.models import Count
# result = (Project.objects.values('status').annotate(dcount=Count('status')).order_by())
# result = list(map(lambda x: x["dcount"], result))

        

