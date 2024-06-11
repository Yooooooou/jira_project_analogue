from rest_framework import serializers

from .models import *


class ProjectStatusRefSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStatusRef
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class MemberRoleRefSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberRoleRef
        fields = '__all__'


class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = '__all__'
