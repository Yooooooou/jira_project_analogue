
from django.urls import include, path

urlpatterns = [
    path('', include('project.urls.project_urls')),
    path('', include('project.urls.status_ref_urls')),
    path('', include('project.urls.roles_ref_urls')),
]
