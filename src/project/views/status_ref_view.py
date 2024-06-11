from rest_framework.decorators import api_view
from rest_framework.response import Response

from project.models import ProjectStatusRef
from project.serializers import ProjectStatusRefSerializer


@api_view(['GET'])
def projectStatusList(request):
    statuses = ProjectStatusRef.objects.all()
    serializer = ProjectStatusRefSerializer(statuses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def projectStatusDetail(request, pk):
    status = ProjectStatusRef.objects.get(id=pk)
    serializer = ProjectStatusRef(status, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def projectStatusCreate(request):
    serializer = ProjectStatusRefSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def projectStatusUpdate(request, pk):
    status = ProjectStatusRef.objects.get(id=pk)
    serializer = ProjectStatusRefSerializer(instance=status, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def projectStatusDelete(request, pk):
    status = ProjectStatusRef.objects.get(id=pk)
    status.delete()
    return Response("status successfully deleted!")
