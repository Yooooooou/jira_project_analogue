from rest_framework import generics

from project.models import ProjectStatusRef
from project.serializers import ProjectStatusRefSerializer


class StatusRefList(generics.ListAPIView):
    queryset = ProjectStatusRef.objects.all()
    serializer_class = ProjectStatusRefSerializer


class StatusRefCreate(generics.CreateAPIView):
    queryset = ProjectStatusRef.objects.all()
    serializer_class = ProjectStatusRefSerializer


class StatusRefUpdate(generics.UpdateAPIView):
    queryset = ProjectStatusRef.objects.all()
    serializer_class = ProjectStatusRefSerializer


class StatusRefDetail(generics.RetrieveAPIView):
    queryset = ProjectStatusRef.objects.all()
    serializer_class = ProjectStatusRefSerializer


class StatusRefDelete(generics.RetrieveDestroyAPIView):
    queryset = ProjectStatusRef.objects.all()
    serializer_class = ProjectStatusRefSerializer
