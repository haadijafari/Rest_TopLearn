from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status, mixins, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from .models import Todo
from .serializers import TodoSerializer, UserSerializer

User = get_user_model()


# region function base apis
@api_view(['GET', 'POST'])
def all_todos(request: Request):
    if request.method == 'GET':
        todos = Todo.objects.order_by('priority').all()
        todo_serializer = TodoSerializer(todos, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        todo_serializer = TodoSerializer(data=request.data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return Response(todo_serializer.data, status.HTTP_201_CREATED)
    return Response(None, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request: Request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        return Response(None, status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        todo_serializer = TodoSerializer(todo, many=False)
        return Response(todo_serializer.data, status.HTTP_200_OK)
    elif request.method == 'PUT':
        todo_serializer = TodoSerializer(todo, data=request.data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return Response(todo_serializer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)


# endregion


# region class base apis
class TodoListApiView(APIView):
    def get(self, request: Request):
        todos = Todo.objects.order_by('priority').all()
        todo_serializer = TodoSerializer(todos, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)

    def post(self, request: Response):
        todo_serializer = TodoSerializer(data=request.data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return Response(todo_serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(None, status.HTTP_400_BAD_REQUEST)


class TodoDetailApiView(APIView):
    def get(self, request: Request, todo_id: int):
        todo = get_object_or_404(Todo, pk=todo_id)
        todo_serializer = TodoSerializer(todo, many=False)
        return Response(todo_serializer.data, status.HTTP_200_OK)

    def put(self, request: Request, todo_id: int):
        todo = get_object_or_404(Todo, pk=todo_id)
        todo_serializer = TodoSerializer(todo, data=request.data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return Response(todo_serializer.data, status.HTTP_202_ACCEPTED)
        else:
            return Response(None, status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, todo_id: int):
        todo = get_object_or_404(Todo, pk=todo_id)
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)


# endregion

# region class base apis using mixins
class TodoListMixinApiView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request: Response):
        return self.create(request)


class TodoDetailMixinApiView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                             generics.GenericAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer

    def get(self, request: Request, pk: int):
        return self.retrieve(request, pk)

    def put(self, request: Request, pk: int):
        return self.update(request, pk)

    def delete(self, request: Request, pk: int):
        return self.destroy(request, pk)


# endregion

# region class base apis using generics
class TodoListApiPagination(PageNumberPagination):
    page_size = 3


class TodoListGenericApiView(generics.ListCreateAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
    pagination_class = TodoListApiPagination


class TodoDetailGenericApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer


class UserListGenericApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = TodoListApiPagination


# endregion

# region class base apis using view sets
class TodoViewSetApiView(viewsets.ModelViewSet):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
    pagination_class = TodoListApiPagination

# endregion
