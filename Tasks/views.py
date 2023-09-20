from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class TaskListCreateView(generics.ListCreateAPIView):
    """
    View to create new or getting list of all Tasks.
    """
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retreive/get or update or delete specific task by passing their pk/{id}.
    """
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskSortListView(generics.ListAPIView):
    """ 
    View to Sort tasks based on due_date and title.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        sort_by = self.request.query_params.get('sort_by', None)
        if sort_by:
            return Task.objects.order_by(sort_by)
        return Task.objects.all()
    

class TaskFilterListView(generics.ListAPIView):
    """
    View to Filter Tasks based on status and due_date.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()

        # Filter by status
        status = self.request.query_params.get('status', None)
        if status:
            queryset = queryset.filter(status=status)

        # Filter by due_date
        due_date = self.request.query_params.get('due_date', None)
        if due_date:
            queryset = queryset.filter(due_date=due_date)

        return queryset