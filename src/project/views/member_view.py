from rest_framework import generics
from project.models import ProjectMember
from project.serializers import ProjectMemberSerializer


class ProjectMemberList(generics.ListAPIView):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer


class ProjectMemberDetail(generics.RetrieveAPIView):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer


class ProjectMemberCreate(generics.CreateAPIView):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer


class ProjectMemberUpdate(generics.UpdateAPIView):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer


class ProjectMemberDelete(generics.RetrieveDestroyAPIView):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer
