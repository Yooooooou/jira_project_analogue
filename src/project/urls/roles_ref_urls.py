from django.urls import path
from project.views import roles_ref_view as views

urlpatterns = [
    path('role-list/', views.roleRefList, name='role-list'),
    path('role-detail/<int:pk>/', views.roleRefDetail, name='role-detail'),
    path('role-create/', views.roleRefCreate, name='role-create'),
    path('role-update/<int:pk>/', views.roleRefUpdate, name='role-update'),
    path('role-delete/<int:pk>/', views.roleRefDelete, name='role-delete'),
]
