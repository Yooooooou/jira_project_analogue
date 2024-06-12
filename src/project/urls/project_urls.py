from django.urls import path
from project.views.project_view import ProjectList, ProjectDetail, ProjectCreate, ProjectUpdate, ProjectDelete

urlpatterns = [
    path('projects/', ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
    path('projects/create/', ProjectCreate.as_view(), name='project-create'),
    path('projects/update/<int:pk>/', ProjectUpdate.as_view(), name='project-update'),
    path('projects/delete/<int:pk>/', ProjectDelete.as_view(), name='project-delete'),
]
