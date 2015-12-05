from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, status

from app.models import *
from app.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RiskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer

class RiskProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RiskProject.objects.all()
    serializer_class = RiskProjectSerializer
