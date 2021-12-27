from django.urls import path
from .views import home_view, about_page,student_list

urlpatterns = [
    path('home/', home_view),
    path('list/', student_list)

]


