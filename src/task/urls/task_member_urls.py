from django.urls import path
from task.views.task_member_view import TaskMemberList, TaskMemberDetail, TaskMemberCreate, TaskMemberUpdate, \
    TaskMemberDelete

urlpatterns = [
    path('member/', TaskMemberList.as_view(), name='member-list'),
    path('member/<int:pk>/', TaskMemberDetail.as_view(), name='member-detail'),
    path('member/create/', TaskMemberCreate.as_view(), name='member-create'),
    path('member/update/<int:pk>/', TaskMemberUpdate.as_view(), name='member-update'),
    path('member/delete/<int:pk>/', TaskMemberDelete.as_view(), name='member-delete'),
]
