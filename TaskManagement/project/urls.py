from django.contrib import admin
from django.urls import path, include
from project.views import CreateProjectView
from project.views import ListProjectView


urlpatterns = [
    path("create-project", CreateProjectView.as_view(), name="create-project"),
    path("list-project", ListProjectView.as_view(), name="list-project"),
]
