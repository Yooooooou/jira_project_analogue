from django.urls import path
from project.views.roles_ref_view import RoleRefList, RoleRefDetail, RoleRefCreate, RoleRefUpdate, RoleRefDelete

urlpatterns = [
    path('roles/', RoleRefList.as_view(), name='role-list'),
    path('roles/<int:pk>/', RoleRefDetail.as_view(), name='role-detail'),
    path('roles/create/', RoleRefCreate.as_view(), name='role-create'),
    path('roles/update/<int:pk>/', RoleRefUpdate.as_view(), name='role-update'),
    path('roles/delete/<int:pk>/', RoleRefDelete.as_view(), name='role-delete'),
]
