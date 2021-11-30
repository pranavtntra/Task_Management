from django.urls import path
from timeline.views import Dashboard, ActiveProjects, Employee_report, EmployeePdf, ProjectStatusReport, \
                            ProjectStatusPdf, CompleteProjectReport, ActiveProjectReport, SprintReport, \
                            CompleteProjectPdf, ActiveProjectPdf

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('active_projects/', ActiveProjects.as_view(), name="active_projects"),
    path('employee_report/', Employee_report.as_view(), name="employee_report"),
    path('employee_pdf/', EmployeePdf.as_view(), name="employee_pdf"),
    path('project_status_report/', ProjectStatusReport.as_view(), name="project_status_report"),
    path('project_status_pdf/', ProjectStatusPdf.as_view(), name="project_status_pdf"),
    path('complete_project_report/', CompleteProjectReport.as_view(), name="complete_project_report"),
    path('complete_project_pdf/', CompleteProjectPdf.as_view(), name="complete_project_pdf"),
    path('active_project_report/', ActiveProjectReport.as_view(), name="active_project_report"),
    path('active_project_pdf/', ActiveProjectPdf.as_view(), name="active_project_pdf"),
    path('sprint_report/', SprintReport.as_view(), name="sprint_report")
]
