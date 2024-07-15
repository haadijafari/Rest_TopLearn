from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_todos, name='all_todos'),
    path('<int:todo_id>', views.todo_detail, name='todo_detail'),
]
