from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from critics import models
from .serializers import CriticSerializer

class CriticViewSet(viewsets.ModelViewSet):
    queryset = models.Critic.objects.all()
    serializer_class = CriticSerializer