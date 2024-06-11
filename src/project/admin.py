from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ProjectStatusRef)
admin.site.register(Project)
admin.site.register(MemberRoleRef)
admin.site.register(ProjectMember)
