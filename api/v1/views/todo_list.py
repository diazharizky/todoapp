from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Todo
from api.v1.serializers.todo import TodoSerializer


class TodoListApiView(APIView):
    def get(self, request):
        todos = Todo.objects
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            "task": request.data.get("task"),
            "completed": request.data.get("completed"),
        }

        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
