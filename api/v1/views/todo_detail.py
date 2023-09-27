from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Todo
from api.v1.serializers.todo import TodoSerializer


class TodoDetailApiView(APIView):
    def get_object(self, todo_id):
        try:
            return Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return None

    def get(self, request, todo_id):
        todo_instance = self.get_object(todo_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = TodoSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
