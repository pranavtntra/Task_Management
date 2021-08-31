from django.contrib import admin
from django.urls import path, include
from project.views import CreateProjectView
from project.views import ListProjectView
from project.views import SearchProjectView
from project.views import SortProjectView, AddEmployeeView, ViewEmployeeView


urlpatterns = [
    path("create-project", CreateProjectView.as_view(), name="create-project"),
    path("list-project", ListProjectView.as_view(), name="list-project"),
    path("search-project", SearchProjectView.as_view(), name="search-project"),
    path("sort-project", SortProjectView.as_view(), name="sort-project"),
    path("add-member", AddEmployeeView.as_view(), name="add-member"),
    path("view-member", ViewEmployeeView.as_view(), name="view-member"),
]
