from rest_framework.decorators import api_view
from rest_framework.response import Response

from project.models import MemberRoleRef
from project.serializers import MemberRoleRefSerializer




@api_view(['GET'])
def roleRefList(request):
    roles = MemberRoleRef.objects.all()
    serializer = MemberRoleRefSerializer(roles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def roleRefDetail(request, pk):
    roles = MemberRoleRef.objects.get(id=pk)
    serializer = MemberRoleRefSerializer(roles, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def roleRefCreate(request):
    serializer = MemberRoleRefSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def roleRefUpdate(request, pk):
    role = MemberRoleRef.objects.get(id=pk)
    serializer = MemberRoleRefSerializer(instance=role, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def roleRefDelete(request, pk):
    role = MemberRoleRef.objects.get(id=pk)
    role.delete()
    return Response("project successfully deleted!")