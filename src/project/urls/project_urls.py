from django.urls import path
from project.views import project_view as views

urlpatterns = [
    path('project-list/', views.projectList, name='project-list'),
    path('project-detail/<int:pk>/', views.projectDetail, name='project-detail'),
    path('project-create/', views.projectCreate, name='project-create'),
    path('project-update/<int:pk>/', views.projectUpdate, name='project-update'),
    path('project-delete/<int:pk>/', views.projectDelete, name='project-delete'),
]
