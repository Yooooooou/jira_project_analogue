from rest_framework import generics
from project.models import Project
from project.serializers import ProjectSerializer


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectCreate(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectUpdate(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDelete(generics.RetrieveDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
