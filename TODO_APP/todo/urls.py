from django.urls import path
from .views import home, todo_list

urlpatterns = [
    path('home/', home, name = 'house'),
    path('list/', todo_list, name = 'list')
]