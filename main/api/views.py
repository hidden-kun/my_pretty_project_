from main.models import Task
from django import *
from main.api.serializers import TaskModelSerializer
from rest_framework import viewsets , filters




class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter ]
    

