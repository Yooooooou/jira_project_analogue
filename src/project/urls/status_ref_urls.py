from django.urls import path
from project.views import status_ref_view as views

urlpatterns = [
    path('status-list/', views.projectStatusList, name='status-list'),
    path('status-detail/<int:pk>/', views.projectStatusDetail, name='status-detail'),
    path('status-create/', views.projectStatusCreate, name='status-create'),
    path('status-update/<int:pk>/', views.projectStatusUpdate, name='status-update'),
    path('status-delete/<int:pk>/', views.projectStatusDelete, name='status-delete'),
]
