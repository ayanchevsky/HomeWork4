from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from .serializers import *
from .models import Todo


class MyOffsetPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10


# Create your views here.
class Todos(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodosSerializer
    pagination_class = MyOffsetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['title']
    ordering_fields = ['__all__']

    def post(self, request):
        print(request)
        title = request.data.get('title', None)
        description = request.data.get('description', None)
        if title and description:
            Todo(title=title, description=description, created_date=timezone.now()).save()
            return Response({'Create': 'Success'})
        else:
            return Response({'Create': 'Failed'})


class OneTodo(APIView):
    pagination_class = MyOffsetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['title', 'completed']
    ordering_fields = ['__all__']

    def get_object(self, pk):
        return Todo.objects.get(pk=pk)

    def get(self, request, pk):
        obj = self.get_object(pk)
        ser = TodoDetailSerializer(obj)
        return Response(ser.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        obj = self.get_object(pk)
        ser = TodosSerializer(obj, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            Response(ser.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        todo = get_object_or_404(Todo, id=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#
# def home(request):
#     return render(request, 'home.html')
#
#
# def currenttodos(request):
#     todos = Todo.objects.filter(completed=False)
#     content = {'todos': todos}
#     return render(request, 'currenttodos.html', content)
#
# def completetodos(request):
#     todos = Todo.objects.filter(completed=True)
#     content = {'todos': todos}
#     return render(request, 'completetodos.html', content)
#
#
# def alltodos(request):
#     todos = Todo.objects.all()
#     content = {'todos': todos}
#     return render(request, 'alltodos.html', content)
#
#
# def createtodo(request):
#     if request.method == 'GET':
#         content = {'form': TodoForm()}
#         return render(request, 'createtodo.html', content)
#     else:
#         form = TodoForm(request.POST)
#         form.save()
#         return redirect('currenttodos')
#
#
# def viewtodo(request, todo_id):
#     todo = get_object_or_404(Todo, id=todo_id)
#     if request.method == 'GET':
#         form = TodoForm(instance=todo)
#         content = {'todo': todo,
#                    'form': form}
#         return render(request, 'viewtodo.html', content)
#     else:
#         form = TodoForm(request.POST, instance=todo)
#         todo.completed_date = None if todo.completed else timezone.now()
#         form.save()
#         return redirect('currenttodos')
#
#
# def completetodo(request, todo_id):
#     todo = get_object_or_404(Todo, id=todo_id)
#     if request.method == 'POST':
#         todo.completed_date = timezone.now()
#         todo.completed = True
#         todo.save()
#         return redirect('alltodos')
#
#
# def continuetodo(request, todo_id):
#     todo = get_object_or_404(Todo, id=todo_id)
#     if request.method == 'POST':
#         todo.completed_date = None
#         todo.completed = False
#         todo.save()
#         return redirect('alltodos')
#
#
# def deletetodo(request, todo_id):
#     todo = get_object_or_404(Todo, id=todo_id)
#     if request.method == 'POST':
#         todo.delete()
#         return redirect('alltodos')