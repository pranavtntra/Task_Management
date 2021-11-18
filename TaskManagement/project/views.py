from django.shortcuts import render
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView
from project.forms import CreateProjectForm, AddMemberForm, ProjectUpdateForm
from project.models import Project, ProjectTeam
from django.urls import reverse_lazy
from accounts.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .services import get_projects
import logging
from .constants import SORTER
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class CreateProjectView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "project/create_project.html"
    form_class = CreateProjectForm

    def get_form(self, *args, **kwargs):
        form = super(CreateProjectView, self).get_form(*args, **kwargs)
        try:
            form.fields['project_lead'].queryset = User.objects.filter(
                is_superuser=False)
        except Exception as e:
            logging.error(str(e))
        return form


class ListProjectView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "project/list_project.html"
    context_object_name = "projectlist"

    def get_queryset(self):
        try:
            return get_projects(self.request.user)
        except Exception as e:
            logging.error(str(e))


class SearchProjectView(View):

    def get(self, request, *args, **kwargs):
        search = self.request.GET.get('search')
        start = self.request.GET.get('start_date')
        end = self.request.GET.get('end_date')
        selected = self.request.GET.get('sort')

        projectlist = get_projects(self.request.user)
        try:
            projectlist = projectlist.filter(Q(title__icontains=search) | Q(
                project_lead__username__icontains=search))
            if start and end:
                projectlist = projectlist.filter(
                    Q(start_date__gte=start) & Q(end_date__lte=end))
            if selected:
                projectlist = projectlist.order_by(SORTER[selected])

            proj_list = {
                "search_projectlist": projectlist,
                "error_message": 'No such data found'
            }

        except Exception as e:
            logging.error(str(e))
            proj_list = {"search_projectlist": projectlist}
        return render(request, "project/listproject.html", proj_list)


@method_decorator(csrf_exempt, name='dispatch')
class AddEmployeeView(View):
    def get(self, request):
        proj_id = self.request.GET.get('proj')
        proj_obj = Project.objects.get(id=proj_id)
        form = AddMemberForm()
        context = {"form": form, "proj_title": proj_obj.title,
                   "proj_id": str(proj_obj.id)}
        html_form = render_to_string('project/add_member.html',
                                     context=context
                                     )
        return JsonResponse({"form": html_form})

    def post(self, request):
        data = dict()
        form = AddMemberForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.project = Project.objects.get(id=request.POST.get("project"))
            obj.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False

        context = {'form': form}
        data['html_form'] = render_to_string('project/add_member.html',
                                             context,
                                             request=request
                                             )
        return JsonResponse(data)


class ViewEmployeeView(View):
    def get(self, request):
        proj_id = self.request.GET.get('proj')
        proj_obj = Project.objects.get(id=proj_id)
        team = ProjectTeam.objects.filter(project=proj_obj)
        context = {"proj_title": proj_obj.title,
                   "proj_id": str(proj_obj.id), "team": team}
        html_form = render_to_string('project/view_member.html',
                                     context=context
                                     )

        return JsonResponse({"form": html_form})


class UpdateProjectView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectUpdateForm
    template_name = 'project/update_project.html'
    success_url = reverse_lazy('listproject')


class DeleteProjectView(DeleteView):
    model = Project
    success_url = reverse_lazy('listproject')
