"""API views"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Todo
from api.serializers import TodoSerializer


class TodoListApiView(APIView):
    """TodoListApiView class"""

    def get(self, request):
        """Get todo"""

        todos = Todo.objects
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Create a todo"""

        data = {
            "task": request.data.get("task"),
            "completed": request.data.get("completed"),
        }

        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailApiView(APIView):
    """TodoDetailApiView class"""

    def get_object(self, todo_id):
        """No comment"""

        try:
            return Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return None

    def get(self, request, todo_id):
        """Get todo detail"""

        todo_instance = self.get_object(todo_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = TodoSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
