from django.urls import path
from .views import home_view,student_list,student_updated,student_detail,student_delete, student_update,student_add

urlpatterns = [
    path('home/', home_view, name = 'home'),
    path('list/', student_list, name = 'list'),
    path('add/', student_add, name = 'add'),
    path('<int:id>', student_detail, name = 'detail'),
    path('<int:id>/delete', student_delete, name = 'delete'),
    path('<int:id>/update', student_update, name='update'),
    path('<int:id>/updated', student_updated, name='updated'),

]


