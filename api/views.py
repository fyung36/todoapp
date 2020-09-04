from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/all_task/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/create_task/',
        'Update':'/edit_task/<str:pk>/',
        'Delete':'/delete-task/<str:pk>'
    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    task = Task.objects.all()
    serizializer =TaskSerializer(task, many=True)
    data = serizializer.data
    return Response(data)

@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serizializer =TaskSerializer(task, many=False)
    data = serizializer.data
    return Response(data)

@api_view(['POST'])
def createTask(request):
    serizializer =TaskSerializer(data=request.data)
    if serizializer.is_valid():
        serizializer.save()
    data = serizializer.data
    return Response(data)

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serizializer =TaskSerializer(instance=task, data=request.data)
    if serizializer.is_valid():
        serizializer.save()
    data = serizializer.data
    return Response(data)

@api_view(['DELETE'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Task Was deleted Successfully")






