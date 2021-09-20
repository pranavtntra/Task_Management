from django.urls import path
from timeline.views import Dashboard

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
]
