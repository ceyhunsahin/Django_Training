from django.urls import path
from .views import home_api, student_list_api

urlpatterns = [
    path('home_api/', home_api),
    path('list_api/', student_list_api)
]