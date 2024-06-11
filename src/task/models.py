from django.db import models
from django.contrib.auth.models import User
from project.models import Project


class TaskStatus(models.Model):
    code = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=100)


class Task(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_task')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE, to_field='code')


class TaskMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

