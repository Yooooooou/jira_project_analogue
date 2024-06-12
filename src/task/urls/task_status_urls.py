from django.urls import path
from task.views.task_status_view import TaskStatusList, TaskStatusDetail

urlpatterns = [
    path('task-status/', TaskStatusList.as_view(), name='task-list'),
    path('task-status/<int:pk>/', TaskStatusDetail.as_view(), name='task-detail'),
]
