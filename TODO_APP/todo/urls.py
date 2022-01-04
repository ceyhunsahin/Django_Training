from django.urls import path
from .views import home, todo_list,todo_delete, todo_create, todo_update

urlpatterns = [
    path('home/', home, name = 'house'),
    path('list/', todo_list, name = 'list'),
    path('create/', todo_create, name = 'create'),
    path('<int:id>/update/', todo_update, name = 'update'),
    path('<int:id>/delete/', todo_delete, name = 'delete')
]