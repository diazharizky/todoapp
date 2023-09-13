"""A file that contains serializers"""

from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """Todo serializer"""

    class Meta:
        """Meta method"""

        model = Todo
        fields = ["id", "task", "completed", "timestamp", "updated"]
