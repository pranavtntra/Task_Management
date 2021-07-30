from django.urls import path
from task.views import CreateTaskView, TaskListView, CreateSubTaskView, TaskDetailView, ProjectListView

urlpatterns = [
    path('add_task/', CreateTaskView.as_view(), name="add_task"),
    path('task_list/', TaskListView.as_view(), name="task_list"),
    path('add_subtask/', CreateSubTaskView.as_view(), name="add_subtask"),
    path('task_detail/<int:pk>/', TaskDetailView.as_view(), name="task_detail"),
    path('project_tasklist/', TaskListView.as_view(), name="project_tasklist"),

]
