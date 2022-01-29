from rest_framework import serializers
# from django.contrib.auth.models import User, Group
from critics import models


class CriticSerializer(serializers.ModelSerializer):
    class Meta:
        
        fields = (
            'id',
            'title',
            'description',
            'food',
            'overall',
        )


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['user', 'username', 'email', 'groups']

# class GroupSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model = Group
#         fields = ['url', 'name']

model = models.Critic 