from django.urls import path
from .views.todo_list import TodoListApiView
from .views.todo_detail import TodoDetailApiView

urlpatterns = [
    path("todos", TodoListApiView.as_view()),
    path("todos/<int:todo_id>/", TodoDetailApiView.as_view()),
]
