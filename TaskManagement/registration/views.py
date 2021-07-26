from django.views.generic import TemplateView

# Create your views here.


class Home(TemplateView):
    template_name = "tests/index.html"


class Dashboard(TemplateView):
    template_name = "tests/dashboard.html"
