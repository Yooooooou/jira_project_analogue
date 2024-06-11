from django.db import models
from django.contrib.auth.models import User


class ProjectStatusRef(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=200)


class Project(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(ProjectStatusRef, on_delete=models.CASCADE)


class MemberRoleRef(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=200)


class ProjectMember(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='members')
    role = models.ForeignKey(MemberRoleRef, on_delete=models.CASCADE)
