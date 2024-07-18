from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_todos, name='all_todos'),
    path('<int:todo_id>', views.todo_detail, name='todo_detail'),
    path('cbv', views.TodoListApiView.as_view(), name='all_todos_cbv'),
    path('cbv/<int:todo_id>', views.TodoDetailApiView.as_view(), name='todo_detail_mixin'),
    path('mixins', views.TodoListMixinApiView.as_view(), name='all_todos_cbv'),
    path('mixins/<int:pk>', views.TodoDetailMixinApiView.as_view(), name='todo_detail_mixin'),
]
