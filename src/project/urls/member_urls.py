from django.urls import path
from project.views.member_view import ProjectMemberList, ProjectMemberDetail, ProjectMemberCreate, ProjectMemberUpdate, ProjectMemberDelete

urlpatterns = [
    path('members/', ProjectMemberList.as_view(), name='member-list'),
    path('members/<int:pk>/', ProjectMemberDetail.as_view(), name='member-detail'),
    path('members/create/', ProjectMemberCreate.as_view(), name='member-create'),
    path('members/update/<int:pk>/', ProjectMemberUpdate.as_view(), name='member-update'),
    path('members/delete/<int:pk>/', ProjectMemberDelete.as_view(), name='member-delete'),
]
