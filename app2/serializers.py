from rest_framework import serializers
from .models import taskBoard

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=taskBoard
        fields='__all__'