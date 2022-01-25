from rest_framework import serializers
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
        model = models.Critic