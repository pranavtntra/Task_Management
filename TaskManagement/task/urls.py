from django.urls import path
from task.views import CreateTaskView, TaskListView

urlpatterns = [
    path('add_task/', CreateTaskView.as_view(), name="add_task"),
    path('task_list/', TaskListView.as_view(), name="task_list" ),
    path('task_list/', TaskListView.as_view(), name="task_list" ),
]