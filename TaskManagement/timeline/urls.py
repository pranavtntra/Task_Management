from django.urls import path
from timeline.views import Dashboard, ActiveProjects

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('active_projects/', ActiveProjects.as_view(), name="active_projects"),
]
