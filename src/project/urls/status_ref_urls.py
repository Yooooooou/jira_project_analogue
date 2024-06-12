from django.urls import path
from project.views.status_ref_view import StatusRefList, StatusRefDetail, StatusRefCreate, StatusRefUpdate, \
    StatusRefDelete

urlpatterns = [
    path('status/', StatusRefList.as_view(), name='status-list'),
    path('status/<int:pk>/', StatusRefDetail.as_view(), name='status-detail'),
    path('status/create/', StatusRefCreate.as_view(), name='status-create'),
    path('status/update/<int:pk>/', StatusRefUpdate.as_view(), name='status-update'),
    path('status/delete/<int:pk>/', StatusRefDelete.as_view(), name='status-delete'),
]
