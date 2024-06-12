
from django.urls import include, path

urlpatterns = [
    path('', include('task.urls.task_urls')),
    path('', include('task.urls.task_status_urls')),
    path('', include('task.urls.task_member_urls')),
]
