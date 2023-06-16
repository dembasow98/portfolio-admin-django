from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.

class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()