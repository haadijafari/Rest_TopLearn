from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('view_sets', views.TodoViewSetApiView)

urlpatterns = [
    path('', views.all_todos, name='all_todos'),
    path('<int:todo_id>', views.todo_detail, name='todo_detail'),
    path('cbv', views.TodoListApiView.as_view(), name='all_todos_cbv'),
    path('cbv/<int:todo_id>', views.TodoDetailApiView.as_view(), name='todo_detail_mixin'),
    path('mixins', views.TodoListMixinApiView.as_view(), name='all_todos_cbv'),
    path('mixins/<int:pk>', views.TodoDetailMixinApiView.as_view(), name='todo_detail_generic'),
    path('generics', views.TodoListGenericApiView.as_view(), name='all_todos_cbv'),
    path('generics/<int:pk>', views.TodoDetailGenericApiView.as_view(), name='todo_detail_generic'),
    path('', include(router.urls), name='todo_view_set'),
]
