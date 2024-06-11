from rest_framework.decorators import api_view
from rest_framework.response import Response

from project.models import Project
from project.serializers import ProjectSerializer




@api_view(['GET'])
def projectList(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def projectDetail(request, pk):
    projects = Project.objects.get(id=pk)
    serializer = ProjectSerializer(projects, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def projectCreate(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def projectUpdate(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(instance=project, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def projectDelete(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    return Response("project successfully deleted!")