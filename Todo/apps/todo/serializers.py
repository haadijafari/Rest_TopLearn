from django.contrib.auth import get_user_model
from rest_framework import serializers

from . import models

User = get_user_model()


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Todo
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    todo_set = TodoSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = '__all__'
