from django.urls import path
from task.views import CreateTaskView, CreateSubTaskView, SearchTaskView, TaskListView, ProjectTaskListView, TaskList

urlpatterns = [
    path('add_task/', CreateTaskView.as_view(), name="add_task"),
    path('add_subtask/', CreateSubTaskView.as_view(), name="add_subtask"),
    path('mytask_list/', TaskListView.as_view(), name="mytask_list"),
    path('project_tasklist/', ProjectTaskListView.as_view(), name="project_tasklist"),
    path('tasklist/', TaskList.as_view(), name="tasklist"),
    path('search_task/', SearchTaskView.as_view(), name= "search_task"),
]
