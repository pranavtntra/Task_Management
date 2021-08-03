from django.urls import path
from task.views import CreateTaskView, CreateSubTaskView, TaskListView, ProjectTaskListView, TaskList

urlpatterns = [
    path('add_task/', CreateTaskView.as_view(), name="add_task"),
    path('add_subtask/', CreateSubTaskView.as_view(), name="add_subtask"),
    path('task_list/', TaskListView.as_view(), name="task_list"),
    path('project_tasklist/', ProjectTaskListView.as_view(), name="project_tasklist"),   
    path('tasklist/', TaskList.as_view(), name='tasklist'),
]
