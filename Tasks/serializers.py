from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Seraializer to serialize the Task model querysets or instances into python objects.
    """
    class Meta:
        model = Task
        fields = '__all__'
