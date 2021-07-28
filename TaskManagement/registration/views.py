from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args,
                                                        **kwargs)


class Home(TemplateView):
    template_name = "tests/index.html"


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "tests/dashboard.html"
