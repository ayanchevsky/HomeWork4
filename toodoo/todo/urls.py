from django.urls import path
from todo.views import Todos, OneTodo

urlpatterns = [
    path('tasks/', Todos.as_view()),
    path('tasks/<pk>/', OneTodo.as_view()),
]