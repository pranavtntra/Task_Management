from django.contrib import admin
from django.urls import path, include
from project.views import CreateProjectView
from project.views import ListProjectView
from project.views import SearchProjectView
from project.views import SortProjectView, AddEmployeeView, ViewEmployeeView,SearchDateProjectView,UpdateProjectView,DeleteProjectView


urlpatterns = [
    path("createproject", CreateProjectView.as_view(), name="createproject"),
    path("listproject", ListProjectView.as_view(), name="listproject"),
    path("search-project", SearchProjectView.as_view(), name="search-project"),
    path("sort-project", SortProjectView.as_view(), name="sort-project"),
    path("add-member", AddEmployeeView.as_view(), name="add-member"),
    path("view-member", ViewEmployeeView.as_view(), name="view-member"),
    path("searchdate-project", SearchDateProjectView.as_view(), name="searchdate-project"),
    path('updateproject/<int:pk>/', UpdateProjectView.as_view(), name='updateproject'),
    path('deleteuser/<int:pk>/', DeleteProjectView.as_view(), name='deleteproject'),


]
