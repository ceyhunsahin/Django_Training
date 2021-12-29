from django.urls import path
from .views import home_api, student_list_create_api
print('ceyhun')
urlpatterns = [
    path('home_api/', home_api),
    # path('list_api/', student_list_api),
    # path('create_api/', student_create_api)
    path('list_create_api/', student_list_create_api),
]