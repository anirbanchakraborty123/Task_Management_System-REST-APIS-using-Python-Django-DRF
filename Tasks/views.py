from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    """
    View to create new or getting list of all Tasks.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retreive/get or update or delete specific task by passing their pk/{id}.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer