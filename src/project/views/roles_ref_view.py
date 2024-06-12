from rest_framework import generics
from project.models import MemberRoleRef
from project.serializers import MemberRoleRefSerializer


class RoleRefList(generics.ListAPIView):
    queryset = MemberRoleRef.objects.all()
    serializer_class = MemberRoleRefSerializer


class RoleRefDetail(generics.RetrieveAPIView):
    queryset = MemberRoleRef.objects.all()
    serializer_class = MemberRoleRefSerializer


class RoleRefCreate(generics.CreateAPIView):
    queryset = MemberRoleRef.objects.all()
    serializer_class = MemberRoleRefSerializer


class RoleRefUpdate(generics.UpdateAPIView):
    queryset = MemberRoleRef.objects.all()
    serializer_class = MemberRoleRefSerializer


class RoleRefDelete(generics.RetrieveDestroyAPIView):
    queryset = MemberRoleRef.objects.all()
    serializer_class = MemberRoleRefSerializer
