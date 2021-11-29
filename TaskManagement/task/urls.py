from django.urls import path
from task.views import CreateTaskView, CreateSubTaskView, UpdateStatus, SearchTaskView, TaskSubListView, TaskListView, TaskListBetweenDates, ProjectTaskListView, TaskList, TaskDetailView, CreateSprint
from . import views

urlpatterns = [
    path('add_task/', CreateTaskView.as_view(), name="add_task"),
    path('add_subtask/', CreateSubTaskView.as_view(), name="add_subtask"),
    path('mytask_list/', TaskListView.as_view(), name="mytask_list"),
    path('project_tasklist/', ProjectTaskListView.as_view(),
         name="project_tasklist"),
    path('tasklist/', TaskList.as_view(), name="tasklist"),
    path('tasksublist/', TaskSubListView.as_view(), name="tasksublist"),
    path('search_task/', SearchTaskView.as_view(), name="search_task"),
    path('task_detail/<int:pk>/', TaskDetailView.as_view(), name="task_detail"),
    path('searchbydates/', TaskListBetweenDates.as_view(), name='searchbydates'),
    path('ajax/load_task/', views.load_task, name='ajax_load_task'),
    path('updatestatus/', UpdateStatus.as_view(), name="updatestatus"),
    path('load_message', views.load_message, name="load_message"),
    path('add_sprint/', CreateSprint.as_view(), name="add_sprint"),
]
