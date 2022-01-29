from django.shortcuts import render
# from django.contrib.auth.models import User, Group
# Create your views here.

from rest_framework import viewsets

from critics import models
from .serializers import CriticSerializer


class CriticViewSet(viewsets.ModelViewSet):
    queryset = models.Critic.objects.all()
    serializer_class = CriticSerializer
    # permission_classes = [IsAuthenticated]

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = models.User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]

# class GroupViewSet(viewsets.ModelViewSet):
#     queryset = models.Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [IsAuthenticated]

