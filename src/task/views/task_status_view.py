from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from task.models import TaskStatus
from task.serializers import TaskStatusSerializer


class TaskStatusList(ListCreateAPIView):
    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerializer


class TaskStatusDetail(RetrieveUpdateDestroyAPIView):
    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerializer
