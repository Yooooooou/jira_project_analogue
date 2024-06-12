from rest_framework import generics

from task.models import TaskMember
from task.serializers import TaskMemberSerializer


class TaskMemberList(generics.ListAPIView):
    queryset = TaskMember.objects.all()
    serializer_class = TaskMemberSerializer


class TaskMemberDetail(generics.RetrieveAPIView):
    queryset = TaskMember.objects.all()
    serializer_class = TaskMemberSerializer


class TaskMemberCreate(generics.CreateAPIView):
    queryset = TaskMember.objects.all()
    serializer_class = TaskMemberSerializer


class TaskMemberUpdate(generics.UpdateAPIView):
    queryset = TaskMember.objects.all()
    serializer_class = TaskMemberSerializer


class TaskMemberDelete(generics.RetrieveDestroyAPIView):
    queryset = TaskMember.objects.all()
    serializer_class = TaskMemberSerializer
